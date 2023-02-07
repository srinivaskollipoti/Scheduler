# Importing the required modules
import json
import logging

from message_queue.consumer import MessageQueue
from service.service_scheduler import ServiceScheduler

# Initializing an instance of the ServiceScheduler class
service_scheduler = ServiceScheduler()

# Defining a callback function that will be used to process messages received from the message queue
def callback(channel, method, properties, payload) -> None:
    try:
        logging.debug(" [x] Received %s" % payload)
        print(" [x] Received %s" % payload)

        # Decoding the payload and converting it to a Python object
        payload = json.loads(payload.decode())

        # Adding the customer information to the service scheduler
        service_scheduler.add_customer(payload)

        # Acknowledging the message as processed
        channel.basic_ack(delivery_tag=method.delivery_tag)

        logging.debug("Message processed from the checkin_queue")
    except Exception as e:
        logging.error("Unable to process the message from queue")


if __name__ == "__main__":
    messageQueue = MessageQueue()

    # Receiving messages from the queue and passing them to the callback function
    messageQueue.recieve(callback)
