class Student:


    def __init__(self, name, father_name, gender, mobile, email, address, course, admission_date, student_id=None):

        self.student_id = student_id
        self.name = name
        self.father_name = father_name
        self.gender = gender
        self.mobile = mobile
        self.email = email
        self.address = address
        self.course = course
        self.admission_date = admission_date