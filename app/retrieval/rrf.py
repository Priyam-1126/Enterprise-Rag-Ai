class ReciprocalRankFusion:

    @staticmethod
    def fuse(
        dense,
        sparse,
        k=60,
    ):

        scores = {}

        for rank, row in enumerate(dense):

            idx = row["id"]

            scores[idx] = scores.get(
                idx,
                0,
            ) + 1 / (k + rank + 1)

        for rank, row in enumerate(sparse):

            idx = row["id"]

            scores[idx] = scores.get(
                idx,
                0,
            ) + 1 / (k + rank + 1)

        ranking = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranking