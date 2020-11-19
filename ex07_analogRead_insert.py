import pymysql as ps
import time
import spidevRead as sr

db = ps.connect(
    host="localhost",
    user="root",
    passwd="1234",
    db="test")

curs = db.cursor()

while True:
    readData = sr.analog_read(0)
    sql = f'insert into sensordb(sensing) values(readData);'
    curs.execute(sql)
    db.commit()
    time.sleep(5)
    
