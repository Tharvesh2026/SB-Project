import pika

url = "amqps://zoujmvkl:CrqgUcZBc7e6NCJ6G3HNNI0gd7NEhos-@chameleon.lmq.cloudamqp.com/zoujmvkl"

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='hello')
bodyMsg = input("Enter message to send: ")
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=bodyMsg
)

print("Message sent")

connection.close()