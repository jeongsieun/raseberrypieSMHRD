import pymysql as ps


db = ps.connect(
    host="localhost",
    user="root",
    passwd="1234",
    db="test")

curs = db.cursor()
sql = 'insert into sensordb(sensing) values(1023);'
curs.execute(sql)
db.commit()
