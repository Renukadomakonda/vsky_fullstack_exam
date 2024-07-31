import paho.mqtt.client as mqtt

# MQTT broker details
broker = 'test.mosquitto.org'
port = 1883
topic = 'restaurant/orders'

# Callback when a message is received
def on_message(client, userdata, message):
    order = message.payload.decode()
    print(f"Received `{order}` from topic `{message.topic}`")

def main():
    # Create an MQTT client instance
    client = mqtt.Client()
    # Connect to the broker
    client.connect(broker, port)
    
    # Set the message callback
    client.on_message = on_message

    # Subscribe to the topic
    client.subscribe(topic)

    # Start the loop
    client.loop_forever()

if __name__ == '__main__':
    main()
