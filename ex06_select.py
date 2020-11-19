import pymysql as ps

db = ps.connect(
    host="localhost",
    user="root",
    passwd="1234",
    db="test")

curs = db.cursor()
def slt():
    sql = 'select * from sensordb;'
    curs.execute(sql)
    result = curs.fetchall()
    r = '<br>'.join(map(str, result))
    return r
