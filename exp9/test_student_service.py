import unittest
from unittest.mock import Mock

from student_service import StudentService

class TestStudentService(unittest.TestCase):

    def test_get_student_name(self):

        # Create Mock Database
        mock_database = Mock()

        # Define fake return value
        mock_database.get_student.return_value = {
            "id": 1,
            "name": "Priya",
            "course": "AI"
        }

        # Inject mock object
        service = StudentService(mock_database)

        result = service.get_student_name(1)

        self.assertEqual(result, "Priya")

        # Verify method call
        mock_database.get_student.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()