from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.chat import ChatRequest
from app.database.db import get_db

from app.retrieval.hybrid_search import HybridRetriever
from app.retrieval.rrf import ReciprocalRankFusion

from app.agents.planner import Planner
from app.agents.reranker import reranker
from app.agents.answerer import AnswerGenerator

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):

    try:

        # Step 1: Query Planning
        sub_queries = Planner.split(request.question)

        all_documents = []

        # Step 2: Hybrid Retrieval
        for query in sub_queries:

            results = HybridRetriever.search(
                db=db,
                question=query,
            )

            dense_results = results["dense"]
            sparse_results = results["sparse"]

            # Step 3: Reciprocal Rank Fusion
            ReciprocalRankFusion.fuse(
                dense_results,
                sparse_results,
            )

            # Step 4: Merge duplicate documents
            unique_docs = {}

            for doc in dense_results:
                unique_docs[doc["id"]] = doc

            for doc in sparse_results:
                unique_docs[doc["id"]] = doc

            # Step 5: Rerank
            reranked = reranker.rerank(
                query,
                list(unique_docs.values()),
            )

            all_documents.extend(
                reranked[:5]
            )

        # Remove duplicate chunks
        seen = set()
        final_documents = []

        for doc in all_documents:
            if doc["id"] not in seen:
                seen.add(doc["id"])
                final_documents.append(doc)

        # Step 6: Generate Answer
        answer = AnswerGenerator.generate(
            request.question,
            final_documents,
        )

        # Step 7: Return Response
        return {
            "question": request.question,
            "answer": answer,
            "retrieved_documents": len(final_documents),
            "citations": [
                {
                    "chunk_id": doc["id"],
                    "score": doc.get("rerank_score", 0),
                }
                for doc in final_documents[:5]
            ],
        }

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )