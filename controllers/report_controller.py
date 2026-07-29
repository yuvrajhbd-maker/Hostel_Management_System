from dao.reportdao import ReportDAO
from utils.export import export_excel, export_pdf


class ReportController:
    """All report-related business logic lives here. The view should only
    call methods on this class -- it should never import ReportDAO or the
    export utilities directly."""

    STUDENT_HEADERS = ["ID", "Name", "Father", "Mobile", "Course", "Date"]
    ROOM_HEADERS = ["Room No", "Type", "Capacity", "Occupied", "Status"]
    FEE_HEADERS = ["Student", "Total", "Paid", "Due", "Date", "Mode"]

    def __init__(self):
        self.dao = ReportDAO()

    def student_report(self):
        return self.STUDENT_HEADERS, self.dao.student_report()

    def room_report(self):
        return self.ROOM_HEADERS, self.dao.room_report()

    def fee_report(self):
        return self.FEE_HEADERS, self.dao.fee_report()

    def export_excel(self, filename, headers, data):
        if not data:
            raise ValueError("First Open Any Report")
        export_excel(filename, headers, data)

    def export_pdf(self, filename, headers, data):
        if not data:
            raise ValueError("First Open Any Report")
        export_pdf(filename, headers, data)
