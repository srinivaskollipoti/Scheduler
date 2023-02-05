from typing import Any

import mysql.connector


class DatabaseHandle:
    """
    Class to manage the connection to a MySQL database.
    """

    def __init__(self) -> None:
        """
        Initialize the database connection.
        """
        pass

    def client(self) -> Any:
        """
        Connect to the MySQL database.

        Returns:
            A MySQL connection object.
        """
        self.connection = mysql.connector.connect(
            user="root", password="root", host="mysql", port="3306", database="db"
        )
        return self.connection

    def close(self) -> None:
        """
        Close the MySQL connection.
        """
        self.connection.close()
