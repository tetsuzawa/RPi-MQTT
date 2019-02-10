#coding: utf-8
import paho.mqtt.client as mqtt
import time
import os, sys
#path = os.path.join(os.path.dirname(__file__), '../')
#sys.path.append(path)
#from password.password import *

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.tls_set('/etc/ssl/certs/ca-certificates.crt')
client.username_pw_set(os.environ["CLOUD_MQTT_USERNAME"], os.environ["CLOUD_MQTT_PASSWORD"])
client.connect(os.environ["CLOUD_MQTT_URL"], int(os.environ["CLOUD_MQTT_SSL_PORT"]), keepalive=60)
#client.username_pw_set(CLOUD_MQTT_USERNAME, CLOUD_MQTT_PASSWORD)
#client.connect(CLOUD_MQTT_URL, CLOUD_MQTT_SSL_PORT, keepalive=60)



def pub_test():

    for i in range(0,5):
        client.publish('control', 'test' + str(i))
        time.sleep(1)

def pub_main():

        pub_test()
 
#client.loop_start()
if __name__ == "__main__":
    pub_main()