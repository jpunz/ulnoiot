import time
import paho.mqtt.client as mqtt
from threading import Thread
import signal
from random import randint

print("Partymode is running....")

def party_function():
#    while True:
    for x in range(0,300):
        val1 = randint(0,255)
        val2 = randint(0,255)
        val3 = randint(0,255)
        client.publish("ledstrip/ledstrip/rgb/set",str(val1)+","+str(val2)+","+str(val3))
        print("light on")
        time.sleep(0.05)
        client.publish("ledstrip/ledstrip/rgb/set",str(0)+","+str(0)+","+str(0))
        print("light off")
        time.sleep(0.05)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("bdop/partymode/set")

def on_message(client, userdata, msg):
    if str(msg.payload) == "on":
        print("partymode is now on")
        thread.start()
    else:
        print("partymode is off")


client = mqtt.Client()
client2 = mqtt.Client()

thread = Thread(target=party_function)

client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.12.1",1883,60)
client2.connect("192.168.12.1",1883,60)


client.loop_forever()