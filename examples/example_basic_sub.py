"""
MIT License

Copyright (c) 2022 Phil Tyler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------------------------------------------------------------------------
Project Site: https://github.com/laidbackcoder/EssentialMQTT
-------------------------------------------------------------------------------
"""

from src.essentialmqtt import mqtt_client
from time import sleep

client_id = 'test_client_2'
broker = '127.0.0.1'
topic = 'easy_mqtt/test/value1'

# Define a callback to be executed upon topic value change
def on_message(msg):
    # Print any topic value changes to the console
    print("Received: {} ({})".format(msg.payload.decode(), msg.topic))

mqtt = mqtt_client(client_id, broker)
mqtt.connect()
mqtt.subscribe_to_topic(topic, on_message)

# Keep connection open for 60 seconds
sleep(60)

mqtt.disconnect()