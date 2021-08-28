import sqlite3

conn = sqlite3.connect('test1.db') #建立/連結資料庫test1
cu = conn.cursor() #必要指令，讓python可以控制SQLite


def Create_New_Table():
  #在資料庫test1中建立資料表weather
  #資料表weather包含四個數據，no:項目、time:資料寫入時間、temp:溫度、rain:雨量
  #建立資料表只需要執行一次，之後才能進行下面的新增/修改/查詢/刪除 資料的動作
  cu.execute("create table weather(no,time,temp,rain)")

  
def Insert_New_Data():
  #新增資料，假設有一筆資料在14:10:06觀測，得到溫度32，雨量12，則可以列:
  cu.execute("insert into weather values ('1','14:10:06',32.0,12)")
  #須注意有string跟int、float等資料格式的差別
  
  #每次變動(新增/修改/查詢/刪除)資料表都要加下行
  conn.commit()
  
def Update_Data():
  #假設在項目no= 1 的欄位中，更改他的溫度temp為28，注意這兩個值一個是string，一個是number:
  cu.execute("update weather set temp = 28 where no = '1'")
  conn.commit()
  
  #假設想一次更改兩個或以上的值，如再把rain改為14，可以以逗號分隔:
  #cu.execute("update weather set temp = 28, rain = 14 where no = '1'")
  #conn.commit()
  
  #假設更改的值為變數x1、x2、x3、x4，可以利用format語法撰寫:
  #例如，在項目1中，把溫度、雨量、時間都用變數值更改，使用語法如下
  #x1 = 1 #項目
  #x2 = 18 #溫度
  #x3 = 50 #雨量
  #x4 = '21:17:56' #時間
  #cu.execute("update weather set temp = {b}, rain = {c}, time= '{d}' where no = '{a}'".format(a=x1,b=x2,c=x3,d=x4))
  #conn.commit()
  
def D_Data():
  #刪除資料，其實就是用Updata的方式將全部/部分資料變成空值(NULL)
  #如果是刪除"部分"，那就先找出指定要刪除的項目，再利用Update_Data()的方式將no = 1的資料改成NULL即可
  #如果要刪除"全部"，可參照:
  cu.execute("select count(*) from weather")
  n = int(cu.fetchall()[0][0])  #找出資料表weather中有多少項

  for i in range(1, n + 1):  #將每一項的時間、溫度、雨量都刪除，只留下項目
      cu.execute("update weather set time = NULL,temp = NULL,rain = NULL where  no = '{a}'".format(a=i))
      conn.commit()
      
      
def Select_Data():
  #查詢資料，列出資料表weather中全部項目:
  cu.execute("select * from weather")
  print(cu.fetchall())

cu.close()
