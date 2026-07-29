from dao.dashboarddao import DashboardDAO


class DashboardController:
    """Assembles the summary numbers shown on the dashboard."""

    def __init__(self):
        self.dao = DashboardDAO()

    def get_summary(self):
        return {
            "total_students": self.dao.total_students(),
            "total_rooms": self.dao.total_rooms(),
            "available_rooms": self.dao.available_rooms(),
            "total_collection": self.dao.total_collection(),
            "total_due_fee": self.dao.total_due_fee(),
        }
