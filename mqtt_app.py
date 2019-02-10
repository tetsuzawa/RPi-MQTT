import paho.mqtt.client as mqtt
 
from password.password import *


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("isyjp/msg1st")
 
def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.tls_set("/etc/ssl/certs/ca-certificates.crt")
 
client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_SSL_PORT)
 
client.loop_forever()