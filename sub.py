# coding: utf-8
import paho.mqtt.client as mqtt
import os
import re
from os.path import join, dirname
from dotenv import load_dotenv

from modules.led_flash_class import Flash

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def on_connect(client, userdata, flags, respons_code):
    print('Connected with result code '+str(respons_code))
    print('Connected to cloudMQTT')
    client.subscribe('#')

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    print(msg.topic+' '+message)
    
    blue = Flash(COUNT=5, BCM_NUM=13)
    yellow = Flash(COUNT=5, BCM_NUM=19)

    if message == 'alternately':
        yellow.flash()
        blue.flash()
    if message == 'yellow':
        yellow.flash()
    if message == 'blue':
        blue.flash()

    del blue
    del yellow

def sub_main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set('/etc/ssl/certs/ca-certificates.crt')
    client.username_pw_set(os.environ["CLOUD_MQTT_USERNAME"], os.environ["CLOUD_MQTT_PASSWORD"])
    client.connect(os.environ["CLOUD_MQTT_URL"], int(os.environ["CLOUD_MQTT_SSL_PORT"]), keepalive=60)
    client.loop_forever()


if __name__ == '__main__':
    sub_main()
