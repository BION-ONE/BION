# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
publish.single("IT4030/topic1", "Hello world!", hostname="test.mosquitto.org")
#publish.single("IT4030/topic1", "Hello world!", hostname="broker.hivemq.com")
print("Done")
