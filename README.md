# EssentialMQTT
An easy to use Python module with just the essentials for working with MQTT[^1].


## :wrench: Installation
```
pip install essentialmqtt
```


## :computer: Basic Usage

### Setup & Connect to the MQTT Broker
```
from essentialmqtt import mqtt_client

client_id = 'test_client_1'
broker = '127.0.0.1'
topic = 'essentialmqtt/test/value1'


mqtt = mqtt_client(client_id, broker)
mqtt.connect()

...
```

### Subscribe to a Topic
```
# Define a callback to be executed upon topic value change
def on_message(msg):
    # e.g. Print any topic value changes to the console
    print("Received: {} ({})".format(msg.payload.decode(), msg.topic))

mqtt.subscribe_to_topic(topic, on_message)

...
```


### Publish to a Topic
```
mqtt.publish_message(topic, "topic value")

...
```

### Disconnect from the MQTT Broker
```
...

mqtt.disconnect()
```

See [Examples](https://github.com/laidbackcoder/EssentialMQTT/tree/master/examples) for more information


## :thumbsup: Additional Credits

This project is built upon the [Paho MQTT](https://www.eclipse.org/paho/index.php?page=clients/python/index.php) Python Module from eclipse.



[^1]: https://mqtt.org/
