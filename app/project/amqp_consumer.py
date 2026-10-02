from pika.adapters import blocking_connection
from amqp_utils.amqp_client import get_conn
import time

def proces_messege(channal: blocking_connection.BlockingConnection, method, properties, body: bytes):
    print(body.decode())
    time.sleep(2)
    


def consume_messege(channal: blocking_connection.BlockingConnection):
    QUEUE = "weather"
    channal.basic_consume(
        queue = QUEUE,
        on_message_callback = proces_messege

    )
    channal.start_consuming()

def main_consumer():
    with get_conn() as connection:
        with connection.channel() as channel:
            consume_messege(channel)