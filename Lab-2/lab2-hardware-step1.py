from sense_hat import SenseHat
import time

sense = SenseHat()

black  = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

def show_a():
	sense.show_letter("A", back_colour = black)
	time.sleep(2)

def show_w():
	sense.show_letter("W", back_colour = black)
	time.sleep(2)

show_a()
show_w()

while True:
	events = sense.stick.get_events()
	if events:
		for event in events:
			if event.direction == 'right':
				show_w()
			elif event.direction == 'left':
				show_a()
			elif event.direction == 'up':
				sense.clear()


