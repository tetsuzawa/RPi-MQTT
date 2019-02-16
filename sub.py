# coding: utf-8
import paho.mqtt.client as mqtt
import os
import re

from modules import led_flash
from password.password import *




def on_connect(client, userdata, flags, respons_code):
    print('Connected with result code '+str(respons_code))
    print('Connected to cloudMQTT')
    #client.subscribe('isyjp/msg1st')
    #client.subscribe('control/#')
    client.subscribe('#')

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    #print(msg.topic+' '+str(msg.payload))
    print(msg.topic+' '+message)

    if message == re_compile('on'):
        led_flash.flash()
    if message == re_compile('test0'):
        led_flash.flash()
    if message == re_compile('yellow'):
        led_flash.flash_yellow()
    if message == re_compile('blue'):
        led_flash.flash_blue()

def sub_main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set('/etc/ssl/certs/ca-certificates.crt')
    client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
    client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_SSL_PORT, keepalive=60)
    client.loop_forever()

def re_compile(text):
    text = re.compile(r'%s\s*'%text, re.I)
    return text

if __name__ == '__main__':
    sub_main()