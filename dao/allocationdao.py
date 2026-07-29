from database import get_connection


class AllocationDAO:
    """Raw data-access layer for the `allocation` table. No business logic here."""

    # Allocate Room
    def allocate_room(self, allocation):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            # Check room capacity
            cursor.execute(
                "SELECT capacity, occupied FROM room WHERE room_no=%s",
                (allocation.room_no,)
            )
            room = cursor.fetchone()

            if room is None:
                return "Room Not Found"

            capacity, occupied = room

            if occupied >= capacity:
                return "Room Already Full"

            # Insert Allocation
            query = """
            INSERT INTO allocation
            (student_id, room_no, allocation_date)
            VALUES(%s,%s,%s)
            """

            values = (
                allocation.student_id,
                allocation.room_no,
                allocation.allocation_date
            )

            cursor.execute(query, values)

            # Update Room Occupied Count
            occupied = occupied + 1
            status = "Occupied" if occupied == capacity else "Available"

            update_query = """
            UPDATE room
            SET occupied=%s,
            status=%s
            WHERE room_no=%s
            """

            cursor.execute(update_query, (occupied, status, allocation.room_no))

            conn.commit()
            return "Room Allocated Successfully"
        finally:
            conn.close()

    # View Allocations
    def get_all_allocations(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()

            query = """
            SELECT
            allocation.allocation_id,
            student.name,
            allocation.room_no,
            allocation.allocation_date
            FROM allocation
            INNER JOIN student
            ON allocation.student_id = student.student_id
            """

            cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()

    # Students available for allocation (id + name)
    def get_students(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT student_id, name FROM student")
            return cursor.fetchall()
        finally:
            conn.close()

    # Rooms with free capacity
    def get_available_rooms(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT room_no FROM room WHERE occupied < capacity"
            )
            return cursor.fetchall()
        finally:
            conn.close()
