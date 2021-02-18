#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:20:44 2020

@author: joshyang

MQTT update the command
"""

from __future__ import print_function
import paho.mqtt.publish as publish
import string
import random
import time
from sqlite import *
string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

thinkSpeakApiKey = "AGCAHHWELC6GSQU2"
# Channel ID
channelGroup = "1216894"


#You can use any username.
mqttUsername = "TSMQTTRpiDemo"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "HKJCSDGW9X5SYBON"
tTransport = "websockets"
tPort = 80

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"



# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = channelGroup

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = thinkSpeakApiKey

print(channelID, writeAPIKey)

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey


def main():
# get the system performance data over 20 seconds.

     #Server接收到的訊息

# build the payload string.


# attempt to publish this data to the topic.
    try:
        try:
            status_update = list_all_data()
            payload = "field1" + str(status_update)
            print(payload)
            time.sleep(1)
            clean_data()
            publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
            print (" Published STATUS = ",status_update ," to host: " , mqttHost)

        except Exception as e:
            print("MQTT failed!")
            print(e)


    except:
        print ("There was an error while publishing the data.")
        return False
