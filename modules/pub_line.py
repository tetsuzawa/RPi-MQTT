#coding: utf-8
import paho.mqtt.client as mqtt
import time
import os, sys

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)



client = mqtt.Client(protocol=mqtt.MQTTv311)
client.tls_set('/etc/ssl/certs/ca-certificates.crt')
client.username_pw_set(os.environ["CLOUD_MQTT_USERNAME"], os.environ["CLOUD_MQTT_PASSWORD"])
client.connect(os.environ["CLOUD_MQTT_URL"], int(os.environ["CLOUD_MQTT_SSL_PORT"]), keepalive=60)



def pub_test():
    
    topic = str(input('Enter topic --> '))
    message = str(input('Enter message --> '))
    client.publish(topic, message)
    #for i in range(0,5):
    #    client.publish('control', 'test' + str(i))
    #    time.sleep(1)

def pub_test02(line_message):

    client.publish('control', line_message)

def pub_main():

    pub_test()
 
#client.loop_start()
if __name__ == "__main__":
    pub_test()