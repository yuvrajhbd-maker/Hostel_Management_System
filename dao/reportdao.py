from database import get_connection


class ReportDAO:
    """Raw data-access layer for report queries."""

    def student_report(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT student_id, name, father_name, mobile, course, admission_date
                FROM student
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def room_report(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT room_no, room_type, capacity, occupied, status FROM room"
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def fee_report(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                student.name,
                fee.total_fee,
                fee.paid_amount,
                fee.due_amount,
                fee.payment_date,
                fee.payment_mode
                FROM fee
                INNER JOIN student
                ON fee.student_id = student.student_id
                """
            )
            return cursor.fetchall()
        finally:
            conn.close()
