import MySQLdb

try:
    conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'mydb1', port = 3306)
    cur  = conn.cursor()
    
    cur.execute('select * from account')
    
    cur.close()
    conn.close()
    
except MySQLdb.Error, e:
    print "MySQL Error %d: %s" % (e.args[0], e.args[1])
