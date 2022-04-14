#!/usr/bin/python3

from gpiozero import DistanceSensor
from gpiozero import LED
from time import sleep

led = LED(25)
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2.0)
while True:
	distance = sensor.distance * 100
	print("Distance : %.1f" % distance)
	if distance < 10:
		led.on()
	else:
		led.off()
	sleep(1)
