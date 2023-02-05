import pytest
from unittest.mock import patch
from model.customer import Customer
from mysql_client.client import DatabaseHandle
from dao.checkin_dao import CheckinDao


@patch("mysql_client.client.DatabaseHandle.client")
def test_exception_raised_on_save(mock_connection):
    mock_connection.return_value.cursor.return_value.execute.side_effect = Exception("Save failed")
    checkin_dao = CheckinDao()
    customer = Customer("John", "Doe", "555-555-5555", True)
    
    with pytest.raises(Exception) as excinfo:
        checkin_dao.save_and_retrieve(customer)
        
    mock_connection.return_value.cursor.return_value.execute.assert_called_once()

@patch("mysql_client.client.DatabaseHandle.client")
def test_exception_raised_on_connection(mock_connection):
    mock_connection.side_effect = Exception("Cannot connect to database")
    checkin_dao = CheckinDao()
    customer = Customer("John", "Doe", "555-555-5555", True)
    
    with pytest.raises(Exception) as excinfo:
        checkin_dao.save_and_retrieve(customer)
        
    assert str(excinfo.value) == "Cannot connect to database"
