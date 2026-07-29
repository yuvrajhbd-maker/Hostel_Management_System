class Fee:


    def __init__(
        self,
        student_id,
        total_fee,
        paid_amount,
        due_amount,
        payment_date,
        payment_mode,
        fee_id=None
    ):

        self.fee_id = fee_id
        self.student_id = student_id
        self.total_fee = total_fee
        self.paid_amount = paid_amount
        self.due_amount = due_amount
        self.payment_date = payment_date
        self.payment_mode = payment_mode