import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='pedidos')

for i in range(1, 11):
    mensagem = f"Pedido #{i}"
    channel.basic_publish(
        exchange='',
        routing_key='pedidos',
        body=mensagem
    )
    print(f"[PRODUTOR] Enviado: {mensagem}")

connection.close()