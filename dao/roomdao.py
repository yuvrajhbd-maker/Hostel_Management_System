from database import get_connection


class RoomDAO:
    """Raw data-access layer for the `room` table. No business logic here."""

    # ================= ADD ROOM =================
    def save(self, room):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO room
            (room_no, room_type, capacity, occupied, status)
            VALUES(%s,%s,%s,%s,%s)
            """

            values = (
                room.room_no,
                room.room_type,
                room.capacity,
                room.occupied,
                room.status
            )

            cursor.execute(query, values)
            conn.commit()
        finally:
            conn.close()

    # ================= VIEW ALL ROOMS =================
    def get_all_rooms(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM room")
            return cursor.fetchall()
        finally:
            conn.close()

    # ================= SEARCH ROOM =================
    def search_room(self, room_no):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            SELECT * FROM room
            WHERE room_no LIKE %s
            """

            cursor.execute(query, ("%" + room_no + "%",))
            return cursor.fetchall()
        finally:
            conn.close()

    # ================= DELETE ROOM =================
    def delete_room(self, room_no):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            # Check allocation first
            cursor.execute(
                "SELECT * FROM allocation WHERE room_no=%s",
                (room_no,)
            )
            result = cursor.fetchone()

            if result:
                return "Room is Allocated, Cannot Delete"

            cursor.execute(
                "DELETE FROM room WHERE room_no=%s",
                (room_no,)
            )
            conn.commit()
            return "Room Deleted Successfully"
        finally:
            conn.close()

    # ================= UPDATE ROOM =================
    def update_room(self, room):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            UPDATE room SET
            room_type=%s,
            capacity=%s,
            occupied=%s,
            status=%s
            WHERE room_no=%s
            """

            values = (
                room.room_type,
                room.capacity,
                room.occupied,
                room.status,
                room.room_no
            )

            cursor.execute(query, values)
            conn.commit()
        finally:
            conn.close()

    # ================= AVAILABLE ROOMS =================
    def get_available_rooms(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM room WHERE occupied < capacity")
            return cursor.fetchall()
        finally:
            conn.close()
