# 2020_LoRa
介紹

-----------------------------------
[gateway]中為Gateway所用到的程式。

rf95_server.py為伺服器主程式

sqlite.py為資料庫控制程式

mqtt_publish.py為發布程式

-----------------------------------
[node]中為Node所用。

node/pyrfm/examples中:

rf95_client.py為節點主程式(包含Relay模式一)

rf95_server.py為Relay模式二

而發布程式碼可在node/pyrfm/lib/ll/ll_rfm9x.py中找到

-----------------------------------
[tools]為資料庫創建/測試工具
