import logging
from typing import Dict

from model.customer import Customer
from mysql_client.client import DatabaseHandle

logging.basicConfig(level=logging.DEBUG)


class CheckinDao:
    """
    Class to insert appointments in the database.
    """

    def __init__(self):
        self.__mysql_client = DatabaseHandle()
        self.SQL_APPOINTMENT_STMNT = (
            "INSERT INTO APPOINTMENT (FIRST_NAME, LAST_NAME, PHONE_NUMBER, VIP) "
            "VALUES (%s, %s,%s, %s); "
        )

    def save_and_retrieve(self, customer: Customer) -> int:
        """
        Inserts a `Customer` instance into the `APPOINTMENT` table and retrieves the ID of the inserted record.

        Args:
        - customer (`Customer`): Customer instance to be inserted into the database.

        Returns:
        - int: ID of the inserted record.

        Raises:
        - Exception: In case of any error while inserting the record into the database.
        """
        connection = self.__mysql_client.client()
        cursor = connection.cursor()
        logging.debug(self.SQL_APPOINTMENT_STMNT)

        fname, lname, number, is_vip = (
            customer.fname,
            customer.lname,
            customer.phone_number,
            customer.is_vip and 1,
        )
        logging.debug(f"Payload values: {fname}, {lname}, {number},{is_vip}")

        try:
            logging.debug("Started inserting records into the APPOINTMENT table")
            cursor.execute(self.SQL_APPOINTMENT_STMNT, (fname, lname, number, is_vip))
            connection.commit()
            appointment_id = cursor.lastrowid
            self.__mysql_client.close()

        except Exception as e:
            logging.error("Unable to insert the record to database", str(e))
            raise e

        logging.debug(f"{cursor.rowcount} record(s) inserted.")

        return appointment_id
