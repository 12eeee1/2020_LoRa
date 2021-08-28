import sqlite3

conn = sqlite3.connect('test1.db')

cu = conn.cursor()

#cu.execute("create table weather(no,temp,rain,co2)")

#cu.execute("insert into weather values (1,32,12,1.0 )")
conn.commit()
cu.execute("select * from weather")
print(cu.fetchall())

cu.close()
