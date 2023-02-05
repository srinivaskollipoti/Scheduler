class Customer:
    """
    Customer class representing the details of a customer.
    """

    def __init__(self, fname: str, lname: str, phone_number: str, is_vip: bool) -> None:
        """
        Initialize the customer object with the given first name, last name, phone number and VIP status.

        :param fname: First name of the customer
        :type fname: str
        :param lname: Last name of the customer
        :type lname: str
        :param phone_number: Phone number of the customer
        :type phone_number: str
        :param is_vip: Boolean indicating whether the customer is a VIP or not
        :type is_vip: bool
        """
        self.fname = fname
        self.lname = lname
        self.phone_number = phone_number
        self.is_vip = is_vip

    def is_valid_input(self) -> bool:
        """
        Check if the customer object has all required fields filled.

        :return: Boolean indicating whether the customer object is valid or not
        :rtype: bool
        """
        if self.fname and self.lname and self.phone_number and self.is_vip is not None:
            return True
        return False
