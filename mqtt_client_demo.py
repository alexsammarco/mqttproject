#MQTT Client demo
#continuously monitor two different MQTT topics for
#Check if the received data matches two predefined 'commands'

import paho.mqtt.client as mqtt

# the callback for when the client receives a CONNACK respone from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #subsribing in on_connect() - if we lose the connection and
    #reconnect the subscriptions will be renewed.
    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")


#The callback for when a publish message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "1":
        print("received message #1,Lazer has been broken!")
        #Alert

#create an MQTT client and attatch our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
