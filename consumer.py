import pika

url = "amqps://zoujmvkl:CrqgUcZBc7e6NCJ6G3HNNI0gd7NEhos-@chameleon.lmq.cloudamqp.com/zoujmvkl"

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Received:", body.decode())

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for messages...")
channel.start_consuming()