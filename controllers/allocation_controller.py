from models.allocation import Allocation
from dao.allocationdao import AllocationDAO


class AllocationController:
    """All room-allocation business logic lives here. The view should only
    call methods on this class -- it should never run raw SQL itself."""

    def __init__(self):
        self.dao = AllocationDAO()

    def get_students(self):
        """Returns list of (student_id, name) tuples."""
        return self.dao.get_students()

    def get_available_rooms(self):
        """Returns list of (room_no,) tuples for rooms with free capacity."""
        return self.dao.get_available_rooms()

    def allocate_room(self, student_id, room_no, allocation_date):
        if student_id is None or room_no is None or not allocation_date:
            raise ValueError("Fill All Details")

        allocation = Allocation(student_id, room_no, allocation_date)
        return self.dao.allocate_room(allocation)

    def get_all_allocations(self):
        return self.dao.get_all_allocations()
