# coding: utf-8
import paho.mqtt.client as mqtt
import os, urllib

CLOUD_MQTT_USERNAME = "abmnbdsi"
CLOUD_MQTT_PASSWORD = "m7C7GWvo4s43"
CLOUD_MQTT_URL = "m16.cloudmqtt.com"
CLOUD_MQTT_PORT = 17684
CLOUD_MQTT_SSL_PORT = 27684
CLOUD_MQTT_WEBSOCKET_TTL_PORT = 37684

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
url = urllib.parse.urlparse(url_str)
topic = url.path[1:] or 'test'

# Connect
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))

"""
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected to cloudMQTT")
    #client.subscribe("isyjp/msg1st")
    client.subscribe("isyjp/msg1st")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
 
client = mqtt.Client(protocol=mqtt.MQTTv311)
print("1")
client.on_connect = on_connect
print("2")
client.on_message = on_message
print("3")
 
client.tls_set("/etc/ssl/certs/ca-certificates.crt")
 
client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_WEBSOCKET_TTL_PORT, keepalive=60)
print("4")  
client.loop_forever()
"""