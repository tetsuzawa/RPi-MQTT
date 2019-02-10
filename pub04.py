#coding: utf-8
import paho.mqtt.client as mqtt
import time
import os
from modules import led_flash
from password.password import *

client = mqtt.Client()

def pub_test():

    for _i in range(0,5):
        client.publish('control', 'test')
        time.sleep(1)

def pub_main():

    client.tls_set('/etc/ssl/certs/ca-certificates.crt')
    #client.username_pw_set(os.environ["CLOUD_MQTT_USERNAME"], os.environ["CLOUD_MQTT_PASSWORD"])
    #client.connect(os.environ["CLOUD_MQTT_URL"], int(os.environ["CLOUD_MQTT_SSL_PORT"]), keepalive=60)
    client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
    client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_SSL_PORT, keepalive=60)

    pub_test()
 
#client.loop_start()
if __name__ == "__main__":
    pub_main()