# coding: utf-8
import paho.mqtt.client as mqtt
from modules import led_flash
from password.password import *
import os


def on_connect(client, userdata, flags, respons_code):
    print('Connected with result code '+str(respons_code))
    print('Connected to cloudMQTT')
    #client.subscribe('isyjp/msg1st')
    client.subscribe('isyjp/#')
 
def on_message(client, userdata, msg):
    print(msg.topic+' '+str(msg.payload))
    print(msg.payload)
    print(type(msg.payload))
    print(msg.payload.decode('utf-8'))
    print(type(msg.payload.decode('utf-8')))
    message = msg.payload.decode('utf-8')
    if message == 'on':
        led_flash.flash()

 
client = mqtt.Client(protocol=mqtt.MQTTv311)
print('1')
client.on_connect = on_connect
print('2')
client.on_message = on_message
print('3')
 
client.tls_set('/etc/ssl/certs/ca-certificates.crt')
client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_SSL_PORT, keepalive=60)
print('4')  
client.loop_forever()