# Importing required modules
import logging
from typing import Dict

from flask import Flask, Response, jsonify, make_response

from service.appointment_service import AppointmentService
from service.service_scheduler import ServiceScheduler

# Creating a Flask app
app = Flask(__name__)

ap_service = AppointmentService()
service_scheduler = ServiceScheduler()

# Defining a route for the API endpoint to get the next customer from the appointment queue
@app.route("/v1/appointment/next", methods=["GET"])
def get_next_customer() -> Dict:
    """
    Get the next customer from the appointment queue.

    Returns:
        Dict: A dictionary containing the next customer's data.

    Raises:
        Exception: If an error occurs while fetching the next customer.
    """
    try:
        next_customer = service_scheduler.get_next_customer()

        if next_customer:
            cid = ap_service.update(next_customer)
            
        return make_response(jsonify(cid), 200)

    except Exception as e:
        logging.error("Error while getting next customer: %s", e)
        return Response(response=str(e), status=500)


if __name__ == "__main__":
    # Running the Flask app with debugging enabled, on host 0.0.0.0 and port 5001
    app.run(debug=True, host="0.0.0.0", port=5001)
