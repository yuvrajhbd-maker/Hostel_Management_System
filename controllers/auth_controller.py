from database import get_connection


class AuthController:
    """Handles admin authentication. The view calls this instead of touching
    the database or SQL directly."""

    def login(self, username, password):
        """Return True if the credentials match a row in `admin`, else False."""
        if not username or not password:
            raise ValueError("Username and password are required")

        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM admin WHERE username=%s AND password=%s",
                (username, password)
            )
            result = cursor.fetchone()
            return result is not None
        finally:
            conn.close()
