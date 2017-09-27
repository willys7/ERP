#!/usr/bin/env python
import pika
import urllib2
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='validation_queue')

def validate_ingredient(data):
    try:
        url = "http://localhost:8008/api-inventory/validateingredient/"
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        print data
        request = urllib2.Request(url, data=json.dumps(data))
        request.add_header("Content-Type", "application/json")
        response = opener.open(request)
        return response.read()
    except Exception, e:
        return str(e)

def on_request(ch, method, props, body):

    print("request", body)
    response = validate_ingredient(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


#Queue Basic implementation

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='validation_queue')
print(" [x] Awaiting Validation Ingredients requests")
channel.start_consuming()
