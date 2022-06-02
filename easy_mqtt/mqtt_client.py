import paho.mqtt.client as client

class mqtt_client:

    def __init__(self, client_id, broker, port=1883, username=None, password=None):
        self.client_id = client_id
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password

        self.client = client.Client(self.client_id)

    def connect(self):
        def on_connect_callback(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code {}\n",format(rc))

        if self.username is not None and self.password is not None:
            self.client.username_pw_set(self.username, self.password)

        self.client.on_connect = on_connect_callback
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

        return self.client.is_connected()

    def disconnect(self):
        def on_disconnect_callback(client, userdata, rc):
            if rc == 0:
                print("Disconnected from MQTT Broker!")
            else:
                print("Failed to disconnect, return code {}\n",format(rc))

        self.client.on_disconnect = on_disconnect_callback
        self.client.loop_stop()
        self.client.disconnect()

        return not self.client.is_connected


    def publish_message(self, topic, msg):
        result = self.client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print("Sent '{}' to topic '{}'".format(msg, topic))
        else:
            print("Failed to send message to topic {topic}".format(topic))

    def subscribe_to_topic(self, topic, on_message):
        def on_message_callback(client, userdata, msg):
            on_message(msg)

        self.client.message_callback_add(topic, on_message_callback)
        self.client.subscribe(topic)

    def unsubscribe_from_topic(self, topic):
        self.client.unsubscribe(topic)
        self.client.message_callback_remove(topic)
