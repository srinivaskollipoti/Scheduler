import logging

from service.priority_service import PrirorityScheduler


class SchedulingService:
    def __init__(self):
        self.priority_scheduler = PrirorityScheduler()
        
    def priority_queue(self):
        """
        Retrieves the next customer to be served.

        Returns
        -------
        Customer
            Customer object representing the next customer to be served.
        """

        try:
            waiting_customers = self.priority_scheduler.fetch_waiting_jobs()
            customers_priority_queue = self.priority_scheduler.process_queue(
                waiting_customers
            )
            return customers_priority_queue

        except Exception as e:
            logging.error(e)
            raise Exception("Unable to retrieve the next customer")
