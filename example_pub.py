from easy_mqtt import mqtt_client
from time import sleep

client_id = 'test_client_1'
broker = '127.0.0.1'
topic = 'easy_mqtt/test/value1'

mqtt = mqtt_client(client_id, broker)
mqtt.connect()

val = 0
while val < 10:
    mqtt.publish_message(topic, val)
    val += 1
    sleep(1)

mqtt.disconnect()