from models.room import Room
from dao.roomdao import RoomDAO


class RoomController:
    """All room-related business logic lives here. The view should only call
    methods on this class -- it should never import RoomDAO directly."""

    def __init__(self):
        self.dao = RoomDAO()

    def add_room(self, room_no, room_type, capacity):
        if room_no == "" or room_type == "" or capacity == "":
            raise ValueError("Fill All Fields")

        try:
            room_no = int(room_no)
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Enter Valid Number")

        room = Room(room_no, room_type, capacity, 0, "Available")
        self.dao.save(room)

    def get_all_rooms(self):
        return self.dao.get_all_rooms()

    def search_room(self, keyword):
        return self.dao.search_room(keyword)

    def delete_room(self, room_no):
        return self.dao.delete_room(room_no)

    def get_available_rooms(self):
        return self.dao.get_available_rooms()
