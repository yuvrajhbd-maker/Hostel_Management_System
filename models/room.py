class Room:


    def __init__(self, room_no, room_type, capacity, occupied=0, status="Available"):

        self.room_no = room_no
        self.room_type = room_type
        self.capacity = capacity
        self.occupied = occupied
        self.status = status