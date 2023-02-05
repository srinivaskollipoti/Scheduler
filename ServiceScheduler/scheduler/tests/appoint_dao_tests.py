import unittest
from dao.appointment_dao import AppointmentDao


class TestAppointmentDao(unittest.TestCase):
    def setUp(self):
        self.appointment_dao = AppointmentDao()

    def test_get_and_update_status(self):
        # Arrange
        expected_output = [{"id": 1, "name": "John", "status": "RESOLVED"}]

        # Act
        result = self.appointment_dao.get_and_update_status()

        # Assert
        self.assertEqual(expected_output, result)

    def test_get_and_update_status_with_no_waiting_appointments(self):
        # Arrange
        expected_output = []

        # Act
        result = self.appointment_dao.get_and_update_status()

        # Assert
        self.assertEqual(expected_output, result)

    def test_get_and_update_status_with_exception(self):
        # Arrange
        self.appointment_dao.__make_sql_stmt = lambda: (None, None)

        # Act and Assert
        with self.assertRaises(Exception):
            self.appointment_dao.get_and_update_status()


if __name__ == "__main__":
    unittest.main()
