from abc import ABC, abstractmethod

from Checkout.Payment.ManagePayments import ManagePayments


class Payment(ManagePayments, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def payment(self, bill_amount):
        pass
