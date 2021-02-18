import sqlite3
import numpy as np

#連接資料庫
conn = sqlite3.connect("/home/pi/new09.db")
cu = conn.cursor()


#更新資料
def insert_data(e):
	#cu.execute("insert into data values('{a}','{b}','{c}')".format(a=e[0],b=e[1],c=e[2]))
	cu.execute("update data set value = '{a}', time = '{b}' where node = '{c}'".format(a=e[2],b=e[1],c=e[0]))
	conn.commit()
	print("Trying to insert the new data...")

#過濾資料(為了檢查當前資料庫是否還有未上傳的節點)
def filter_update():
	cu.execute("select count(*) from data")
	n = int(cu.fetchall()[0][0])

	cu.execute("select * from data")
	d = cu.fetchall()
	filter = np.array(["     "]*n) #設計過濾陣列
	k = 0
	print("現在資料庫內容:")
	for i in d:
		print(i)
		if i[2] is not None:
			filter[k] = i[0]
		else:
			filter[k] = "empty"
		k = k + 1
	return(filter)

#抓取全部資料
def list_all_data():
	cu.execute("select * from data")
	d = cu.fetchall()

	return(d)

#清除資料
def clean_data():
	cu.execute("select count(*) from data")
	n = int(cu.fetchall()[0][0])

	for i in range(1,n+1):
		name = "Node" + str(i)
		cu.execute("update data set value = NULL,time = NULL where  node = '{a}'".format(a=name))
		conn.commit()
	print("********************All data have been deleted!*********************")
