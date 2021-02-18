#!/usb/bin/env python

"""
    send's a message and waits for a response
"""
__author__ = """test"""
__date__ = "2021"
__version__ = "0.1.0"
__license__ = "GPL"
import sys
import os
import time
import array

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
        'type': 'serial_seed',
        'port': '/dev/serial0'  #LoRa要用serial0
    }
}
ll=pyrfm.getLL(conf)

print('HW-Version: ', ll.getVersion())
if ll.setOpModeSleep(True,True): #基礎設置，頻率一定要跟Gateway相同否則無法傳輸
    ll.setFiFo()
    ll.setOpModeIdle()
    ll.setModemConfig('Bw125Cr45Sf128');
    ll.setPreambleLength(8)
    ll.setFrequency(868) #傳輸頻率
    ll.setTxPower(13)

    while True:
        ll.sendStr("Message from Node1") #想要傳送的訊息
        ll.waitPacketSent()

        if ll.waitRX(timeout=3): #處理收到的訊息
            data=ll.recv()
            header=data[0:4]
            msg=data[4:]
            print('header: ',header)
            print('message:',array.array('B', msg).tostring())
#Relay模式一
           # if header[0] != 0 and header[0] != 1:
           #     print("Relay sending...")
           #     ll.sendRelay(data)
           #     ll.waitPacketSent()
        time.sleep(5)     #發送頻率
