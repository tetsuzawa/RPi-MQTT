#coding: utf-8
import paho.mqtt.client as mqtt
import time
import os
import sys
from os.path import join, dirname

try:
    from dotenv import load_dotenv

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

except Exception as e:
    print(e)


client = mqtt.Client(protocol=mqtt.MQTTv311)
client.tls_set('/etc/ssl/certs/ca-certificates.crt')
client.username_pw_set(os.environ["CLOUD_MQTT_USERNAME"], os.environ["CLOUD_MQTT_PASSWORD"])
client.connect(os.environ["CLOUD_MQTT_URL"], int(os.environ["CLOUD_MQTT_SSL_PORT"]), keepalive=60)


def pub_main():
    
    topic = str(input('Enter topic --> '))
    message = str(input('Enter message --> '))
    client.publish(topic, message)

def pub_line_message(line_message):

    client.publish('control', line_message)

def pub_web(http_post_message):
    
    client.publish('control', http_post_message)
 
#client.loop_start()
if __name__ == "__main__":
    pub_main()