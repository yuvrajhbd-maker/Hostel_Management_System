from models.student import Student
from dao.studentdao import StudentDAO


class StudentController:
    """All student-related business logic lives here. The view (GUI) should
    only call methods on this class -- it should never import StudentDAO or
    talk to the database directly."""

    def __init__(self):
        self.dao = StudentDAO()

    def _validate(self, name, father_name, gender, mobile, email, address, course, admission_date):
        if not all([name, father_name, gender, mobile, address, course, admission_date]):
            raise ValueError("Please fill all required fields")

    def add_student(self, name, father_name, gender, mobile, email, address, course, admission_date):
        self._validate(name, father_name, gender, mobile, email, address, course, admission_date)
        student = Student(name, father_name, gender, mobile, email, address, course, admission_date)
        self.dao.save(student)

    def update_student(self, student_id, name, father_name, gender, mobile, email, address, course, admission_date):
        if student_id is None:
            raise ValueError("No student selected")
        self._validate(name, father_name, gender, mobile, email, address, course, admission_date)
        student = Student(name, father_name, gender, mobile, email, address, course, admission_date, student_id)
        self.dao.update_student(student)

    def delete_student(self, student_id):
        if student_id is None:
            raise ValueError("No student selected")
        self.dao.delete_student(student_id)

    def get_all_students(self):
        return self.dao.get_all_students()

    def search_student(self, keyword):
        keyword = (keyword or "").strip()
        if keyword == "":
            return None  # signal to the view: show all students instead
        return self.dao.search_student(keyword)
