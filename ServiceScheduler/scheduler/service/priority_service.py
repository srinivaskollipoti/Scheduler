from collections import deque

from dao.appointment_dao import AppointmentDao


class PrirorityScheduler:
    """
    Class for scheduling appointments based on priority.
    """

    def __init__(self) -> None:
        """
        Constructor to initialize required components.
        """
        self.appointment = AppointmentDao()
        self.priority_queue = deque()
        self.regular_customers = deque()
        self.vip_customers = deque()

    def fetch_waiting_jobs(self):
        """
        Retrieves all waiting appointments from the database.
        """
        return self.appointment.get_and_update_status()

    def process_queue(self, customer_list):
        """
        Processes appointments and schedules them based on priority.
        """
        for customer in customer_list:
            if customer["VIP"]:
                self.vip_customers.append(customer)
            else:
                self.regular_customers.append(customer)
        while self.vip_customers or self.regular_customers:
            if self.vip_customers:
                vips = len(self.vip_customers)
                for _ in range(min(vips, 2)):
                    self.priority_queue.append(self.vip_customers.popleft())
            if self.regular_customers:
                self.priority_queue.append(self.regular_customers.popleft())

        return self.priority_queue
