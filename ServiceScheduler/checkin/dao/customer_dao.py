import logging
from typing import Dict

from mysql_client.client import DatabaseHandle


class CustomerDao:
    """
    Class to connect to the CUSTOMER table in the database.

    Attributes:
    -----------
    __mysql_client : `DatabaseHandle`
        Object of `DatabaseHandle` to interact with the database.
    """

    def __init__(self):
        """
        Initialize the object of `DatabaseHandle`.
        """
        self.__mysql_client = DatabaseHandle()

    def __make_select_statement(self, fname: str, lname: str, number: str) -> str:
        """
        Make the SQL select statement to retrieve the customer details.

        Parameters:
        -----------
        fname : `str`
            First name of the customer.
        lname : `str`
            Last name of the customer.
        number : `str`
            Phone number of the customer.

        Returns:
        --------
        `str`
            SQL select statement.
        """
        SQL_STMT = f"SELECT FIRST_NAME, LAST_NAME, PHONE_NUMBER FROM CUSTOMER WHERE FIRST_NAME='{fname}' AND LAST_NAME='{lname}' AND PHONE_NUMBER='{number}';"
        return SQL_STMT

    def retrieve(self, customer: Dict) -> Dict:
        """
        Retrieve the customer details from the CUSTOMER table.

        Parameters:
        -----------
        customer : `Dict`
            Dictionary containing the customer details.

        Returns:
        --------
        `Dict`
            Dictionary containing the customer details from the CUSTOMER table.

        Raises:
        -------
        Exception
            If there is any error while retrieving the customer details.
        """
        logging.debug("Customer details are listed")
        fname, lname, number, _ = customer.values()
        try:
            cursor = self.__mysql_client.client().cursor(dictionary=True)
            cursor.execute(self.__make_select_statement(fname, lname, number))
            customer_details = cursor.fetchall()
            self.__mysql_client.close()

        except Exception as e:
            logging.error(
                "Unable to retrieve customer details from the CUSTOMER table: %s", str(e)
            )
            raise e

        if not customer_details:
            raise Exception("No customer details found for the given input")

        logging.debug("Successfully retrieved existing customer details.")
        return customer_details
