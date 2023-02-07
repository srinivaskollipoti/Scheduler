import logging

from mysql_client.client import DatabaseHandle


class AppointmentDao:
    """
    A class for retrieving appointments from the database.

    Attributes:
        __mysql_client (DatabaseHandle): An instance of the `DatabaseHandle` class.

    """

    def __init__(self):
        """
        Initializes the `AppointmentDao` class and creates an instance of the `DatabaseHandle` class.
        """
        self.__mysql_client = DatabaseHandle()

    def __make_update_stmt(self):
        """
        Creates the SQL update statement for updating appointments.

        Returns:
            str: The SQL update statement.
        """
        SQL_UPDATE_STMNT = "UPDATE APPOINTMENT SET STATUS = 'RESOLVED' WHERE FIRST_NAME = %s AND LAST_NAME = %s AND PHONE_NUMBER = %s;"

        return SQL_UPDATE_STMNT

    def __make_select_stmt(self):
        """
        Creates the SQL select statement for retrieving the updated appointment.

        Returns:
            str: The SQL select statement.
        """
        SQL_SELECT_STMNT = "SELECT ID,FIRST_NAME,LAST_NAME FROM APPOINTMENT WHERE FIRST_NAME = %s AND LAST_NAME = %s AND PHONE_NUMBER = %s;"

        return SQL_SELECT_STMNT

    def update_status(self, data) -> dict:
        """
        Retrieves the next appointment from the APPOINTMENT table and updates its status to "RESOLVED".

        Returns:
            dict: A list of dictionaries, where each dictionary represents a customer appointment.

        Raises:
            Exception: If an error occurs while updating customer status.
        """
        connection = self.__mysql_client.client()
        update_cursor = connection.cursor()

        SQL_UPDATE_STMNT = self.__make_update_stmt()

        logging.debug(SQL_UPDATE_STMNT)

        try:
            logging.debug("Started updating customer status")
            params = (data["fname"], data["lname"], data["phone_number"])
            update_cursor.execute(SQL_UPDATE_STMNT, params)
            connection.commit()
            self.__mysql_client.close()
        except Exception as e:
            logging.error("Unable to update customer status", str(e))
            raise e

    def retrieve_status_id(self, data) -> dict:
        """
        Retrieves the next appointment from the APPOINTMENT table and updates its status to "RESOLVED".

        Returns:
            dict: A list of dictionaries, where each dictionary represents a customer appointment.

        Raises:
            Exception: If an error occurs while updating customer status.
        """
        select_connection = self.__mysql_client.client()
        select_cursor = select_connection.cursor(dictionary=True)
        SQL_SELECT_STMNT = self.__make_select_stmt()
        logging.debug(SQL_SELECT_STMNT)

        try:
            logging.debug("Started updating customer status")
            params = (data["fname"], data["lname"], data["phone_number"])
            select_cursor.execute(SQL_SELECT_STMNT, params)
            result = select_cursor.fetchall()[-1]
            select_connection.commit()
            self.__mysql_client.close()
            return result or None
        except Exception as e:
            logging.error("Unable to select customer status", str(e))
            raise e
