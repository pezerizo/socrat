from datetime import datetime
import subprocess,sys,socket,struct
import os
import fcntl
sys.path.insert(0, '~/Desktop/socrat')
from _LIB_ import network

class SCANPORT:
    victim_ipl              = None
    min_port                = None
    max_port                = None
    only_success_connection = None
    network_interface       = None
    
    def __init__(self, network_interface):
        self.victim_ipl = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN/SCANPORT\033[0m}:VICTIM-IPL='))
        self.min_port = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN/SCANPORT\033[0m}:FROM-PORT='))
        self.max_port = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN/SCANPORT\033[0m}:TO-PORT='))
        self.only_success_connetion = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN/SCANPORT\033[0m}:Show only open ports(y/n)='))
        if self.only_success_connetion == 'y': self.only_success_connection = True
        else: self.only_success_connection = False
        self.network_interface = network_interface
        self.snpt()
        
    def snpt(self):
        print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: Start')
        print('Ctrl+C to stop')
        for port in range(self.min_port, self.max_port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((self.victim_ipl, port))
                if result == 0:
                    print('[\033[92m+\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: PORT:'+str(port)+'[\033[92mOPEN\033[0m]')
                elif result != 0 and self.only_success_connection == False:
                    print('[\033[91m-\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: PORT:'+str(port)+'[\033[91mCLOSED\033[0m]')
            except KeyboardInterrupt:
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: Stop')
                return 0
                
        print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: Stop')
        return 0

    def __del__(self):
        del self
