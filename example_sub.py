from easy_mqtt import mqtt_client
from time import sleep

client_id = 'test_client_2'
broker = '127.0.0.1'
topic = 'easy_mqtt/test/value1'

def on_message(msg):
    print("Received: {} ({})".format(msg.payload.decode(), msg.topic))

mqtt = mqtt_client(client_id, broker)
mqtt.connect()
mqtt.subscribe_to_topic(topic, on_message)

# Keep connection open for 60 seconds
sleep(60)

mqtt.disconnect()