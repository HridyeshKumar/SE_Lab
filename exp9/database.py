class Database:

    def get_student(self, student_id):
        """
        Simulates fetching student information from a database.
        """
        return {
            "id": student_id,
            "name": "Rahul",
            "course": "B.Tech CSE"
        }