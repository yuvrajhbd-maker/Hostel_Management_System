from database import get_connection


class DashboardDAO:
    """Raw data-access layer for dashboard summary numbers."""

    def total_students(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM student")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def total_rooms(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM room")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def available_rooms(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM room WHERE status='Available'")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def total_collection(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(paid_amount) FROM fee")
            result = cursor.fetchone()[0]
            return result if result is not None else 0
        finally:
            conn.close()

    def total_due_fee(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(due_amount) FROM fee")
            result = cursor.fetchone()[0]
            return result if result is not None else 0
        finally:
            conn.close()
