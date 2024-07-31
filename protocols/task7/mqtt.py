# Write your code here 
import paho.mqtt.client as mqtt
import json
import time

# MQTT broker details
broker = 'test.mosquitto.org'
port = 1883
topic = 'restaurant/orders'

# Data to publish
order = {
    'order_id': '12345',
    'item': 'Pizza',
    'quantity': 2
}

def publish_message(client):
    # Convert order to JSON
    order_json = json.dumps(order)
    # Publish the message
    result = client.publish(topic, order_json)
    status = result[0]
    if status == 0:
        print(f"Sent `{order_json}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def main():
    # Create an MQTT client instance
    client = mqtt.Client()
    # Connect to the broker
    client.connect(broker, port)
    # Start the loop
    client.loop_start()
    
    # Publish a message every 5 seconds
    while True:
        publish_message(client)
        time.sleep(5)

if __name__ == '__main__':
    main()
