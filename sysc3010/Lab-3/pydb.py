#!/usr/bin/env python3
import sqlite3
#Initial Data
date = 'now'
time = 'now'
zone = "garage";
temperature = 15.2;
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#Gaining access to columns by name
dbconnect.row_factory = sqlite3.Row;
#Need a cursor to work with db
cursor = dbconnect.cursor();
for i in range(5):
	date += '1';
	time = '1';
	temperature += 1.1;
	cursor.execute('''insert into temps values(?, ?, ?, ?)''',(date, time, zone, temperature));
#Execute insert Statement
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
	print(row['tdate'], row['ttime'], row['zone'], row['temperature']);
#Close the connection
dbconnect.close();
