'''
This is a very simple script to generate random data and insert it
to a mysql table.
This was tested for a IOT use case
'''

import json
import random
import datetime
import time
import MySQLdb

# Open database connection
db_server_name = "localhost"
db_user = "root"
db_password = "password"
db_schema = "iot"
#db = MySQLdb.connect("localhost","root","password","iot" )
db = MySQLdb.connect(db_server_name,db_user,db_password,db_schema)


deviceNames = ['SBS01', 'SBS02', 'SBS03', 'SBS04', 'SBS05']
#event_dateTime
'''
Table creation Script
SELECT * FROM iot.rand_one;
CREATE TABLE `rand_one` (
  `rand_id` int(11) NOT NULL AUTO_INCREMENT,
  `deviceValue` int(11) DEFAULT NULL,
  `deviceParameter` varchar(45) DEFAULT NULL,
  `deviceId` varchar(45) DEFAULT NULL,
  `event_dateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`rand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

'''

generated_sql = ("INSERT INTO iot.rand_one (deviceValue,deviceParameter,deviceId,event_dateTime) values (")
# generate Flow values
def getFlowValues():
    tempsql = generated_sql
    tempsql = (generated_sql + "{},'Flow','{}','{}');"\
            .format(random.randint(60, 100),random.choice(deviceNames),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return tempsql

# generate Temperature values
def getTemperatureValues():
    tempsql = generated_sql
    tempsql = (generated_sql + "{},'Temperature','{}','{}');"\
            .format(random.randint(15, 35),random.choice(deviceNames),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return tempsql
# generate Humidity values
def getHumidityValues():
    tempsql = generated_sql
    tempsql = (generated_sql + "{},'Humidity','{}','{}');"\
            .format(random.randint(50, 90),random.choice(deviceNames),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return tempsql
# generate Sound values
def getSoundValues():
    tempsql = generated_sql
    tempsql = (generated_sql + "{},'Sound','{}','{}');"\
            .format(random.randint(100, 140),random.choice(deviceNames),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return tempsql
# Generate each parameter's data input in varying proportions

cursor = db.cursor()

while True:
    time.sleep(5)
    rnd = random.random()
    if (0 <= rnd < 0.20):
        data = (getFlowValues())
        print(data)
        number_of_rows = cursor.execute(data)
        db.commit()
    elif (0.20<= rnd < 0.55):
        data = getTemperatureValues()
        print (data)
        number_of_rows = cursor.execute(data)
        db.commit()
    elif (0.55<= rnd < 0.70):
        data = getHumidityValues()
        print (data)
        number_of_rows = cursor.execute(data)
        db.commit()
    else:
        data = getSoundValues()
        print (data)
        number_of_rows = cursor.execute(data)
        db.commit()
db.close()
