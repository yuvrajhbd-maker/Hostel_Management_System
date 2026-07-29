from database import get_connection


class FeeDAO:
    """Raw data-access layer for the `fee` table. No business logic here."""

    # Add Fee
    def save(self, fee):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO fee
            (student_id, total_fee, paid_amount, due_amount, payment_date, payment_mode)
            VALUES(%s,%s,%s,%s,%s,%s)
            """

            values = (
                fee.student_id,
                fee.total_fee,
                fee.paid_amount,
                fee.due_amount,
                fee.payment_date,
                fee.payment_mode
            )

            cursor.execute(query, values)
            conn.commit()
        finally:
            conn.close()

    # View Fee
    def get_all_fee(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            SELECT
            fee.fee_id,
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

            cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()

    # Delete Fee
    def delete_fee(self, fee_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fee WHERE fee_id=%s", (fee_id,))
            conn.commit()
        finally:
            conn.close()

    # Students for the fee-entry dropdown
    def get_students(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT student_id, name FROM student")
            return cursor.fetchall()
        finally:
            conn.close()
