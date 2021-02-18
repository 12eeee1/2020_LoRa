#!/usb/bin/env python

"""
	waits for incomming message and sends response
"""
__author__ = """test"""
__date__ = "2021"
__version__ = "0.1.0"
__license__ = "GPL"
import sys
import os
import array
import time
import datetime

from sqlite import *
from mqtt_publish import *
sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'..'
	)
)

import lib as pyrfm

conf={
	'll':{
		'type':'rfm95'
	},
	'pl':{
		'type':	'serial_seed',

		'port': '/dev/serial0'
	}
}
ll=pyrfm.getLL(conf)

print('HW-Version: ', ll.getVersion())
if ll.setOpModeSleep(True,True): #LoRa基礎設定
	ll.setFiFo()
	ll.setOpModeIdle()
	ll.setModemConfig('Bw125Cr45Sf128');
	ll.setPreambleLength(8)
	ll.setFrequency(868) #節點和伺服器頻率要相同
	ll.setTxPower(13)

	while True: #成功連結LoRa模組之後，等待接收訊號

		if ll.waitRX(timeout=3): #成功接收訊號
			data=ll.recv() #取出資料封包，預設取前四欄
			header=data[0:4]
			msg=data[4:]

			try: #節點將自己的編號回傳給伺服器
				
				n1 = array.array('B', msg).tostring() #節點訊息
				node_name = "Node" + str(header[0])
				node_info = n1.decode('utf-8').split("*")
				node_time = node_info[1]
				node_message = node_info[0]
				message_ = [node_name,node_time,node_message]
				print("Received message is:",message_)
				insert_data(message_) #將資料塞進資料庫
				filter = filter_update() #更新過濾器
				print("Filter is contained:",filter)
				if "empty" not in filter:
					try:
						main() #呼叫MQTT程式
						print("******************************************************")
						print("********************published!************************")
						print("******************************************************")
					except:
						print("publish denied!")
				else:
					print("There are still some empty values in the database, waiting for next round to publish!")
				print("**************************************************************")

			except Exception as e:

				print('update_failed!')
				print(e)
			print('header: ',header)
			print('message:',array.array('B', msg).tostring())
			ll.sendStr('Gateway had gotten your message!') #回傳訊息給節點
