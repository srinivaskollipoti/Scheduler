import json
import logging
from typing import Dict
from flask import Flask, Response, jsonify, make_response, request

from exceptions.customer_exception import CustomerNotFoundException
from exceptions.request_exception import RequestException
from model.customer import Customer
from service.checkin_service import CheckinService
from service.customer_validation_service import CustomerValidationService

PERMITTED_TYPES = ["application/json"]

app = Flask(__name__)
customer_service = CustomerValidationService()
checkin_service = CheckinService()


@app.route("/v1/appointment", methods=["POST"])
def create_appointment() -> Dict:
    """
    Validate incoming request data, create a new customer appointment.

    Returns:
        A dictionary with success/exception message and response code as JSON.
    """
    logging.info("Processing check-in")
    try:
        if request.headers.get("CONTENT_TYPE") not in PERMITTED_TYPES:
            raise RequestException("Content type not permitted")

        fname = request.json.get("firstName")
        lname = request.json.get("lastName")
        phone_number = request.json.get("phoneNumber")
        is_vip = request.json.get("is_vip")
        customer = Customer(fname, lname, phone_number, is_vip)

        if not customer.is_valid_input():
            logging.error(f"Invalid payload to process {customer.__dict__}")
            raise RequestException("Bad request")

        if customer_service.validate(customer):
            checkin_id = checkin_service.checkin(customer)
            return make_response(jsonify({"service_id": checkin_id}), 200)
        else:
            raise CustomerNotFoundException("Customer record not found")

    except RequestException as e:
        logging.error(e)
        return Response(response=str(e), status=400)

    except Exception as e:
        logging.error(f"Error while checking in for service {e}")
        return Response(response=str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
