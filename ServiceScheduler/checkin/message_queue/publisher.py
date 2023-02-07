import logging
import time
from typing import Dict

import pika


def rabbit_mq_heartbeat():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host="rabbitmq")
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("AMQPConnectionError trying again")
            time.sleep(5)
            continue


class MessageQueue:
    """
    Class to configure message queue
    """

    def __init__(self) -> None:
        self.connection = rabbit_mq_heartbeat()

    def publish(self, payload: Dict) -> Dict:
        logging.info("Connected to rabbitmq server......")
        channel = self.connection.channel()
        channel.queue_declare(queue="checkin_queue", durable=True)
        channel.basic_publish(
            exchange="",
            routing_key="checkin_queue",
            body=payload,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )
