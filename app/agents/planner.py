class Planner:

    @staticmethod
    def split(question):

        if " and " in question:

            return [
                q.strip()
                for q in question.split(" and ")
            ]

        return [question]