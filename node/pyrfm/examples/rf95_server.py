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
import threading

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
        'port': '/dev/serial0'
    }
}
ll=pyrfm.getLL(conf)

print('HW-Version: ', ll.getVersion())

if ll.setOpModeSleep(True,True):
    ll.setFiFo()
    ll.setOpModeIdle()
    ll.setModemConfig('Bw125Cr45Sf128');
    ll.setPreambleLength(8)
    ll.setFrequency(868)
    ll.setTxPower(13)
    
    while True:
        
        if ll.waitRX(timeout=3):
            
            data=ll.recv()
            header=data[0:4]
            msg=data[4:]
            print('header: ',header)
            message = array.array('B', msg).tostring()
            print(header[0])
#Relay模式二
            if header[0] == 2:  
            
                print("Received Node" + str(header[0]))
                ll.sendStr(message.decode("utf-8") + 'Message from node1')
