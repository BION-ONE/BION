#MQTT Client

from time import sleep

#import library
import paho.mqtt.client as mqtt

import os

#specify the broker address, it can be IP of raspberry pi or simply localhost
host = "test.mosquitto.org"

#this is the name of topic, like temp
MQTT_TOPIC2 = "topic_humidity"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))


    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
	client.subscribe(MQTT_TOPIC2)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	 print(msg.topic+" "+str(msg.payload))
    	# more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, 1883, 60)
# use this line if you don't want to write any further code.
#It blocks the code forever to check for data
client.loop_forever()