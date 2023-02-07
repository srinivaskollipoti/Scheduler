import logging

from dao.appointment_dao import AppointmentDao


class AppointmentService:
    def __init__(self):
        """
        Initialize the CheckinService.
        """
        self.ad = AppointmentDao()

    def update(self, data) -> bool:
        """
        Check in a customer.

        Parameters
        ----------
        data : Customer data to update
        """
        try:
            self.ad.update_status(data)
            cid = self.ad.retrieve_status_id(data)
            return cid
        except Exception as e:
            logging.debug(f"Unable to update: {e}")
            raise Exception("Unable to update")
