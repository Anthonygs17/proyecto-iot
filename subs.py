import paho.mqtt.client as mqtt
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("actuador")

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    # msg = json.loads(message.payload.decode())
    # print(msg['food'], msg['water'])

# Create a new MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
# Assign the on_message callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Start the MQTT client loop to process network traffic and dispatch callbacks
client.loop_forever()