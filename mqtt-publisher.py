import paho.mqtt.client as mqtt
from random import randrange
import time

mqttBroker ="broker.hivemq.com"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

alert = 0

while True:
    temp = randrange(25,30)
    pressure = randrange(850,900)
    humidity = randrange(10,15)

    if (temp > 28) or (pressure > 870) or (humidity > 12):
        alert = 1
        print("Alert: " + str(alert))
        client.publish("ALERT", alert)

    time.sleep(0.1)
    print("Temprature: " + str(temp))
    client.publish("TEMPERATURE", temp)

    time.sleep(0.1)
    print("Pressure: " + str(pressure))
    client.publish("PRESSURE", pressure)

    time.sleep(0.1)
    print("Humidity: " + str(humidity))
    client.publish("HUMIDITY", humidity)

    print("\n")
    time.sleep(1)
