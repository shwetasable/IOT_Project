import paho.mqtt.client as mqtt
import time

temp = pressure = humidity = alert = 0

def on_message(mqttClient, obj, msg):
	if msg.topic == "ALERT" :
		alert = int(str(msg.payload.decode("utf-8")))
		print("ALERT: Something's out of range.")

	elif msg.topic == "TEMPERATURE" :
		print("Temperature Received: " + str(msg.payload.decode("utf-8")))
		temp = int(str(msg.payload.decode("utf-8")))

	elif msg.topic == "PRESSURE" :
		print("Pressure Received: " + str(msg.payload.decode("utf-8")))
		pressure = int(str(msg.payload.decode("utf-8")))

	elif msg.topic == "HUMIDITY" :
		print("Humidity Received: " + str(msg.payload.decode("utf-8")))
		humidity = int(str(msg.payload.decode("utf-8")))
		print("\n")

mqttClient = mqtt.Client()
mqttClient.on_message = on_message
mqttClient.connect("broker.hivemq.com", 1883, 60)
mqttClient.subscribe("TEMPERATURE", 0)
mqttClient.subscribe("HUMIDITY", 0)
mqttClient.subscribe("PRESSURE", 0)
mqttClient.subscribe("ALERT", 0)
mqttClient.loop_forever()
