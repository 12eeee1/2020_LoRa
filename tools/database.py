
import sqlite3
import numpy as np
#-----------------#
#author = 12eeee
#sqlite test
#-----------------#

#連接資料庫(若名子存在就開啟，否則新建一個資料庫)
conn = sqlite3.connect("new09.db")

#建立游標(讓Python可以控制資料庫)
cu = conn.cursor()

#在資料庫中新建Table，欄位自訂
cu.execute("create table data(node,time,value)")

#在Table更新資料:
#在node= Node3 的欄位中，更改他的value為121
#cu.execute("update data set node = 'Node3' where value = '121'")

#在Table中建立資料
cu.execute("insert into data values('Node1',NULL,NULL)")

#每次更動資料，最後要進行提交
conn.commit() 


#------------------------------------#
#抓取資料(全部)
cu.execute("select * from data")
print(cu.fetchall())
