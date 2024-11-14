import paho.mqtt.client as mqtt
import time
import json

# MQTT settings
broker = 'mqtt.eclipseprojects.io'
port = 1883
topic = 'feeding-data'

# Create MQTT client
client = mqtt.Client()

client.connect(broker, port)

def publish_data(food_level, water_level):
    data = {
        'food': food_level,
        'water': water_level
    }
    payload = json.dumps(data)
    client.publish(topic, payload)
    print(f"Published: {payload}")


try:
    while True:
        food_level = 175
        water_level = 150
        publish_data(food_level, water_level)
        time.sleep(10)
except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()