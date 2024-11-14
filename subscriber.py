import paho.mqtt.client as mqtt
import json
import psycopg2

conn = psycopg2.connect(database="feeding_db",
                            user="postgres",
                            password="tty123",
                            host="localhost",
                            port="5432")

cursor = conn.cursor()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("feeding-data")

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    msg = json.loads(message.payload.decode())
    try:
        cursor.execute("INSERT INTO feeding_data (comida, agua) VALUES (%s, %s);",
            (msg['food'], msg['water']))
    except (Exception, psycopg2.Error) as error:
            print(error.pgerror)
    conn.commit()


# Create a new MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()