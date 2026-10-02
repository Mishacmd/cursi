import time
from pika.adapters import blocking_connection
from amqp_utils.amqp_client import get_conn


def produse_messege(channal: blocking_connection.BlockingConnection) -> None:
    QUEUE = 'weather'
    channal.queue_declare(QUEUE)

    message = 'Misha Nedogonov {item}'
    for item in range(2210):
        time.sleep(0.1)
        channal.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message.format(item=item)
        )
        print(item)


def main_producer():
    with get_conn() as connection:
        with connection.channel() as channel:
            produse_messege(channel)


