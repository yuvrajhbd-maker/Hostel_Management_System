from database import get_connection


class StudentDAO:
    """Raw data-access layer for the `student` table. No business logic here."""

    # Add Student
    def save(self, student):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO student
            (name,father_name,gender,mobile,email,address,course,admission_date)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                student.name,
                student.father_name,
                student.gender,
                student.mobile,
                student.email,
                student.address,
                student.course,
                student.admission_date
            )

            cursor.execute(query, values)
            conn.commit()
        finally:
            conn.close()

    # View All Students
    def get_all_students(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            return cursor.fetchall()
        finally:
            conn.close()

    # Delete Student
    def delete_student(self, student_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            query = "DELETE FROM student WHERE student_id=%s"
            cursor.execute(query, (student_id,))
            conn.commit()
        finally:
            conn.close()

    # Update Student
    # NOTE: previously this method built the query/values but never called
    # cursor.execute()/conn.commit()/conn.close(), so "Update Student" silently
    # did nothing. Fixed below.
    def update_student(self, student):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            UPDATE student SET
            name=%s,
            father_name=%s,
            gender=%s,
            mobile=%s,
            email=%s,
            address=%s,
            course=%s,
            admission_date=%s
            WHERE student_id=%s
            """

            values = (
                student.name,
                student.father_name,
                student.gender,
                student.mobile,
                student.email,
                student.address,
                student.course,
                student.admission_date,
                student.student_id
            )

            cursor.execute(query, values)
            conn.commit()
        finally:
            conn.close()

    # Search Student
    def search_student(self, keyword):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            SELECT * FROM student
            WHERE name LIKE %s
            OR mobile LIKE %s
            """

            value = "%" + keyword + "%"
            cursor.execute(query, (value, value))
            return cursor.fetchall()
        finally:
            conn.close()
