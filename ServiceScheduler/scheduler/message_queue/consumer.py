import logging
import time

import pika


def rabbit_mq_heartbeat():
    """
    Function to handle RabbitMQ heartbeat.
    """
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
    Method to receive messages from the queue.
    :param callback: Callback function to be called when a message is received.
    """

    def __init__(self) -> None:
        self.connection = rabbit_mq_heartbeat()
        self.consumerCallback = None

    def recieve(self, callback):
        self.consumerCallback = callback
        sleepTime = 20
        logging.debug(" [*] Sleeping for ", sleepTime, " seconds.")
        time.sleep(sleepTime)
        logging.debug(" [*] Connecting to server ...")
        channel = self.connection.channel()
        channel.queue_declare(queue="checkin_queue", durable=True)
        logging.debug(" [*] Waiting for messages.")
        channel.basic_qos(prefetch_count=10)
        channel.basic_consume(queue="checkin_queue", on_message_callback=callback)
        channel.start_consuming()
