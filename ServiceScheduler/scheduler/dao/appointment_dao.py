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

    def __make_sql_stmt(self):
        """
        Creates the SQL statements for retrieving and updating appointments.

        Returns:
            tuple: A tuple containing two strings: the SELECT statement and the UPDATE statement.
        """
        SQL_SELECT_STMNT = "SELECT * FROM APPOINTMENT WHERE STATUS = 'WAITING';"
        SQL_UPDATE_STMNT = (
            "UPDATE APPOINTMENT SET STATUS = 'RESOLVED' WHERE STATUS = 'WAITING';"
        )
        return SQL_SELECT_STMNT, SQL_UPDATE_STMNT

    def get_and_update_status(self) -> dict:
        """
        Retrieves the next appointment from the APPOINTMENT table and updates its status to "RESOLVED".

        Returns:
            dict: A list of dictionaries, where each dictionary represents a customer appointment.

        Raises:
            Exception: If an error occurs while retrieving the next appointment.
        """
        connection = self.__mysql_client.client()
        select_cursor = connection.cursor(dictionary=True)
        update_cursor = connection.cursor()

        SQL_SELECT_STMNT, SQL_UPDATE_STMNT = self.__make_sql_stmt()
        logging.debug(SQL_SELECT_STMNT)

        try:
            logging.debug("Started retrieving the next customer")
            select_cursor.execute(SQL_SELECT_STMNT)
            customers_list = select_cursor.fetchall()
            if customers_list:
                update_cursor.execute(SQL_UPDATE_STMNT)
                connection.commit()
            self.__mysql_client.close()

        except Exception as e:
            logging.error("Unable to retrieve the next customer", str(e))
            raise e

        return customers_list
