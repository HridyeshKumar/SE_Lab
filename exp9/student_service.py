class StudentService:

    def __init__(self, database):
        """
        Dependency Injection:
        The database object is passed from outside.
        """
        self.database = database

    def get_student_name(self, student_id):
        student = self.database.get_student(student_id)
        return student["name"]