#!/usr/bin/env python3
import sqlite3
#Initial Data
sensorID = 1;
type = ['door', 'temperature', 'door', 'motion', 'temperature'];
zone = ['kitchen', 'kitchen', 'garage', 'garage', 'garage'];
#Connect to Database file
dbconnect = sqlite3.connect("mydatabase.db");
#Connect Rows 
dbconnect.row_factory = sqlite3.Row;
#Creating cursor
cursor = dbconnect.cursor();
cursor.execute('DELETE FROM sensors');

for i in range(5):
	cursor.execute('''INSERT INTO sensors values(?, ?, ?)''', (sensorID, type[sensorID-1], zone[sensorID-1]));
	sensorID += 1;
dbconnect.commit();
cursor.execute('SELECT * FROM sensors WHERE zone = "kitchen"');
print("The Sensors in the kitchen are: ");
for row in cursor:
	print(row['sensorID'], row['type'], row['zone']);
print("\nAll the door sensors are: ");
cursor.execute('SELECT * FROM sensors WHERE type = "door"');
for row in cursor:
	print(row['sensorID'], row['type'], row['zone']);
dbconnect.close();
