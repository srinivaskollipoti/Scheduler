from dao.customer_dao import CustomerDao
from model.customer import Customer


class CustomerValidationService:
    def __init__(self):
        self.cd = CustomerDao()

    def validate(self, customer: Customer) -> bool:
        """
        Validate if the customer exists in the database.

        Returns
        -------
        bool
            Confirms if the customer exists in the database.
        """
        customer_details = self.cd.retrieve(customer.__dict__)
        if customer_details:
            return True
        return False
