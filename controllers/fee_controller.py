from models.fee import Fee
from dao.feedao import FeeDAO


class FeeController:
    """All fee-related business logic lives here. The view should only call
    methods on this class -- it should never import FeeDAO directly."""

    def __init__(self):
        self.dao = FeeDAO()

    def get_students(self):
        """Returns list of (student_id, name) tuples for the fee form."""
        return self.dao.get_students()

    def add_fee(self, student_id, total_fee, paid_amount, payment_date, payment_mode):
        if student_id is None or total_fee == "" or paid_amount == "":
            raise ValueError("Fill All Fields")

        try:
            total_fee = float(total_fee)
            paid_amount = float(paid_amount)
        except ValueError:
            raise ValueError("Enter Valid Number")

        due_amount = total_fee - paid_amount

        fee = Fee(student_id, total_fee, paid_amount, due_amount, payment_date, payment_mode)
        self.dao.save(fee)

    def get_all_fee(self):
        return self.dao.get_all_fee()

    def delete_fee(self, fee_id):
        self.dao.delete_fee(fee_id)
