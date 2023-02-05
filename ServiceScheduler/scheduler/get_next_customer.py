import json
import logging
from exceptions.empty_queue_exception import EmptyCustomerQueueException
from typing import Dict

from flask import Flask, Response, jsonify, make_response

from cache.cache_service import Cache

app = Flask(__name__)

cache = Cache()


@app.route("/v1/appointment/next", methods=["GET"])
def get_next_customer() -> Dict:
    """
    Get the next customer from the appointment queue
    """
    try:
        next_customer = cache.get_next_customer()
        if not next_customer:
            raise EmptyCustomerQueueException("No customer found in queue")
        return make_response(
            jsonify(next_customer),
            200,
        )

    except Exception as e:
        logging.error(f"Error while getting next customer: {e}")
        return Response(response=str(format(e)), status=500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
