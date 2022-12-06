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

import paho.mqtt.client as client

class mqtt_client:
    """MQTT Client
    """
    def __init__(self, client_id, broker, port=1883, username=None, password=None):
        """MQTT Client

        Args:
            client_id (string): MQTT Client Unique Identifier
            broker (string): MQTT Broker IP Address / URL
            port (int, optional): MQTT Broker Port. Defaults to 1883.
            username (string, optional): MQTT Broker Username. Defaults to None.
            password (string, optional): MQTT Broker Password. Defaults to None.
        """
        self.client_id = client_id
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password

        self.client = client.Client(self.client_id)

    def connect(self, on_connect=None):
        """Connect to MQTT Broker

        Args:
            on_connect (function, optional): Connection Callback. Defaults to None.

        Raises:
            ConnectionException: MQTT Broker Connection and Disconnection Exception.

        Returns:
            bool: Connection Status (True is connected, Fales if Disconnected)
        """
        try:
            def on_connect_callback(client, userdata, flags, rc):
                if rc != 0:
                    raise ConnectionException("Failed to connect, return code {}\n",format(rc))

            if self.username is not None and self.password is not None:
                self.client.username_pw_set(self.username, self.password)

            self.client.on_connect = on_connect_callback
            self.client.connect(self.broker, self.port)
            self.client.loop_start()

            if on_connect is not None:
                on_connect()

            return self.client.is_connected()
        except Exception as e:
            raise ConnectionException("Connection Error - {}", e.message)

    def disconnect(self, on_disconnect=None):
        """Disconnect from MQTT Broker

        Args:
            on_disconnect (function, optional): Disconnection Callback. Defaults to None.

        Raises:
            ConnectionException: MQTT Broker Connection and Disconnection Exception.

        Returns:
            bool: Connection Status (True is connected, Fales if Disconnected)
        """
        try:
            def on_disconnect_callback(client, userdata, rc):
                if rc != 0:
                    raise ConnectionException("Failed to disconnect, return code {}\n",format(rc))

            self.client.on_disconnect = on_disconnect_callback
            self.client.loop_stop()
            self.client.disconnect()

            if on_disconnect is not None:
                on_disconnect()

            return not self.client.is_connected
        except Exception as e:
            raise ConnectionException("Disconnection Error - {}", e.message)

    def publish_message(self, topic, msg):
        """Publish to the MQTT Broker

        Args:
            topic (string): MQTT Topic
            msg (string): Payload Message

        Raises:
            PublishException: MQTT Topic Publish Exception.
        """
        try:
            result = self.client.publish(topic, msg)
            status = result[0]
            if status != 0:
                raise PublishException("Failed to send message to topic {topic}".format(topic))
        except Exception as e:
            raise PublishException("Publish Error - {}", e.message)

    def subscribe_to_topic(self, topic, on_message):
        """Subsctibe to a Topic on the MQTT Broker

        Args:
            topic (string): MQTT Topic
            on_message (function): Message Payload Received Callback

        Raises:
            SubscriptionException: MQTT Topic Subscription and Unsubscription Exception.
        """
        try:
            def on_message_callback(client, userdata, msg):
                on_message(msg)

            self.client.message_callback_add(topic, on_message_callback)
            self.client.subscribe(topic)
        except Exception as e:
            raise SubscriptionException("Subscription Error - {}", e.message)

    def unsubscribe_from_topic(self, topic):
        """Unsubsctibe from a Topic on the MQTT Broker

        Args:
            topic (string): MQTT Topic

        Raises:
            SubscriptionException: MQTT Topic Subscription and Unsubscription Exception.
        """
        try:
            self.client.unsubscribe(topic)
            self.client.message_callback_remove(topic)
        except Exception as e:
            raise SubscriptionException("Unsubscription Error - {}", e.message)


class ConnectionException(Exception):
    """MQTT Broker Connection and Disconnection Exception.

    Args:
        Exception (BaseException): Common base class for all non-exit exceptions.
    """
    pass


class SubscriptionException(Exception):
    """MQTT Topic Subscription and Unsubscription Exception.

    Args:
        Exception (BaseException): Common base class for all non-exit exceptions.
    """
    pass


class PublishException(Exception):
    """MQTT Topic Publish Exception.

    Args:
        Exception (BaseException): Common base class for all non-exit exceptions.
    """
    pass
