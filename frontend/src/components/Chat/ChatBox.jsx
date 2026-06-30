import { useState } from "react";
import ReactMarkdown from "react-markdown";
import api from "../../api/api";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function askQuestion() {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response = await api.post("/chat/", {
        question,
      });

      setAnswer(response.data.answer);
    } catch (err) {
      console.error(err);
      alert("Chat failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-3xl font-bold mb-2">
        🤖 Enterprise AI Assistant
      </h2>

      <p className="text-gray-500 mb-6">
        Ask questions from your uploaded enterprise documents.
      </p>

      <textarea
        rows={4}
        className="w-full border rounded-xl p-4 focus:ring-2 focus:ring-green-500 outline-none"
        placeholder="Example: What is the leave policy?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={askQuestion}
        disabled={loading}
        className="mt-4 bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-xl"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      <div className="mt-8">

        <h3 className="font-bold text-lg mb-3">
          AI Response
        </h3>

        <div className="bg-gray-100 rounded-xl p-5 min-h-[180px] prose max-w-none">

          {answer ? (
            <ReactMarkdown>{answer}</ReactMarkdown>
          ) : (
            <p className="text-gray-500">
              No response yet.
            </p>
          )}

        </div>

      </div>

    </div>
  );
}

export default ChatBox;