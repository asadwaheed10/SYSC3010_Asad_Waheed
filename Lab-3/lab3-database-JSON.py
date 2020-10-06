from urllib.request import *
from urllib.parse import *
import json
import sqlite3

dbconnect = sqlite3.connect("mydatabase.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

#The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=dff371cf7913f43e2bf2bc45ae561a20&units=imperial&q=ottawa
#As of October 2015, you need an API key.
#apiKey = "dff371cf7913f43e2bf2bc45ae561a20"
apiKey = "a808bbf30202728efca23e099a4eecc7"

#Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

#Build the URL Parameters
params = {"q":city, "units":"imperial", "APPID":apiKey}
arguments = urlencode(params)

#Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

webData = urlopen(url)
results = webData.read().decode('utf-8')
#Results is a JSON string
webData.close()

data = json.loads(results)

val = (data["name"], data["main"]["temp"], data["wind"]["speed"])
cursor.execute('''INSERT INTO windy(city, temp, winds) VALUES (?,?, ?)''', val)
dbconnect.commit()

cursor.execute('''SELECT temp, winds FROM windy''')

#Print the results
degreeSym = chr(176)
for row in cursor:
	print ("Temperature: %d%sF" % (row[0], degreeSym))
	print ("Wind: %d" % row[1])

#Close connection
dbconnect.close()
