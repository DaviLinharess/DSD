import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='pedidos')

channel.basic_qos(prefetch_count=1)

print("Consumidor 2 aguardando pedidos...")


def callback(ch, method, properties, body):
    print(f"[Consumidor 2] Recebeu: {body.decode()}")

    time.sleep(2)

    print(f"[Consumidor 2] Pedido processado!")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue='pedidos',
    on_message_callback=callback
)

channel.start_consuming()