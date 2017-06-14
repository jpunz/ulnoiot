#!/usr/bin/env python
# -*- coding: utf8 -*-

import paho.mqtt.client as mqtt
import time
from threading import Thread

unlock = False

def unlock_door(client):
    print "Thread start"
    global unlock
    client.publish("door/lock/set", payload="on", qos=0, retain=False)
    time.sleep(5)
    client.publish("door/lock/set", payload="off", qos=0, retain=False)
    unlock = False

def on_message(client, userdata, msg):            
    global unlock
    print str(msg.payload)
    if not unlock and str(msg.payload) == "198,174,119,65":
        Thread(target=unlock_door, args=(client,)).start()
        unlock = True
        print "Unlock door"
        #unlock_door(client)

def on_connect(client, userdata, flags, rc):
    client.subscribe("door/tagid")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.12.1", 1883, 60)
client.loop_forever()