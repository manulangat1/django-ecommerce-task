import pika

params = pika.URLParameters("")


connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue="order")


def callback(ch, method, properties, body):
    print("received", body)


channel.basic_consume(queue="order", on_message_callback=callback)
print("started consuming")
channel.start_consuming()


channel.close()
