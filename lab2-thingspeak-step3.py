import requests
import threading
import json

import random

# def thingspeak_post():
# 	 threading.Timer(15, thingspeak_post).start()
# 	 val = random.randint(1,30)
#	 URL = 'https://api.thingspeak.com/update?api_key='
#	 KEY = 'IJTZGO1YU2WN8EXU'
#	 HEADER = '&field1={}&field2={}'.format(val,val)
#	 NEW_URL = URL+KEY+HEADER
#	 print(NEW_URL)
#	 data = urrlib.request.urlopen(NEW_URL)
#	 print(data)

def read_data_thingspeak():
	URL = 'https://api.thingspeak.com/channels/1155221/fields/1.json?api_key='
	KEY = 'LBMYHOFDUR5RGS35'
	HEADER = '&results=3'
	NEW_URL = URL+KEY+HEADER
	print (NEW_URL)

	get_data = requests.get(NEW_URL).json()
	field_1 = get_data['feeds']

	t=[]
	for x in field_1:
		t.append(x['field1'])

	print ("The last 3 RPi CPU temperature readings collected on Thingspeak are: ")
	print (temp)

	if __name__ == '__main__':
		read_data_thingspeak()
