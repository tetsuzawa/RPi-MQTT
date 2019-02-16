#coding: utf-8
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect('localhost', 1883, keepalive=60)
client.loop_start()
while True:
  client.publish('world/darai0512', 'test')
  time.sleep(1)