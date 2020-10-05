import http.client
import urllib.parse
import time

key = "54CDA6FJF4RCJ92C"

def thingspeak():
	while True:
		email = "asadwaheed@cmail.carleton.ca"
		group = "L2-M-5"
		identifier = "d"
		params = urllib.parse.urlencode({'field1': email, 'field2': group, 'field3': identifier, 'key': key})
		headers = {"Content-typeZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"} 
		conn = http.client.HTTPConnection("api.thingspeak.com:80")
		try:
			conn.request("POST", "/update", params, headers)
			response = conn.getresponse()
			print (response.status, response.reason)
			data = response.read()
			conn.close()
		except:
			print ("connection failed")
		break
if __name__ == "__main__":
	while True:
		thingspeak()
