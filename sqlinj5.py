import MySQLdb
user = request.GET['username']
#conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="admin",
#passwd="N01WillGue$S",db="clientsDB")
cursor = MySQLdb.connect().cursor()
cursor.execute("select * from customer where username=" + user)
results = cursor.fectchall()
conn.close()
