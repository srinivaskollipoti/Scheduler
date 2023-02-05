import logging

from dao.checkin_dao import CheckinDao
from model.customer import Customer


class CheckinService:
    def __init__(self):
        """
        Initialize the CheckinService.
        """
        self.cr = CheckinDao()

    def checkin(self, customer: Customer) -> bool:
        """
        Check in a customer.

        Parameters
        ----------
        customer : Customer
            Customer object to be checked in.

        Returns
        -------
        bool
            Confirms if the customer was checked in successfully.
        """
        try:
            checkin_id = self.cr.save_and_retrieve(customer)
            if checkin_id:
                return checkin_id
        except Exception as e:
            logging.debug(f"Unable to checkin: {e}")
            raise Exception("Unable to checkin")
        return False
