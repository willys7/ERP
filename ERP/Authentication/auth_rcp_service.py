#!/usr/bin/env python
import pika
import urllib2
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='login_queue')

def auth_user(data):
    url = "http://localhost:8000/api-auth/login/"
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    print data
    rea_data = json.loads(data)
    login = {
        "user_name": rea_data["user_name"],
        "password": rea_data["password"]
    }
    request = urllib2.Request(url, data=json.dumps(login))
    request.add_header("Content-Type", "application/json")
    response = opener.open(request)
    return response.read()

def on_request(ch, method, props, body):

    print("request", body)
    response = auth_user(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


#Queue Basic implementation

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='login_queue')
print(" [x] Awaiting Auth requests")
channel.start_consuming()
