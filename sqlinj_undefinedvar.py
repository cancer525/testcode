import sys
cursor.execute("select * from emp where id="+eid)
row = cursor.fetchone()
self.writeln('Employee name: ' + row["emp"]) 
