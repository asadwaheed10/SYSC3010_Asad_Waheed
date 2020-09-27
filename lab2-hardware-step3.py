#This Program will make use of the SenseHat Temperature Sensors 
#This Program will make use of the SenseHat Display / Joysticks
#This Program was modified code retrieved from an online source - electromaker.io tutorials 

from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def temperature():
	temp = sense.get_temperature()
	print(temp)
	if temp > 34:
		sense.clear(red)
	elif temp > 24 and temp < 34:
		sense.clear(green)
	elif temp < 24:
		sense.clear(blue)
	time.sleep(1)
	sense.show_message(str(round(temp,2)))

while True:
	events = sense.stick.get_events()
	if events:
		for event in events:
			if event.direction == 'right':
				temperature()
			if event.direction == 'up':
				sense.clear()
