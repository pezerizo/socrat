from datetime import datetime
import subprocess,sys,socket,struct
import os
import fcntl
import random 
import time
import sys
sys.path.insert(0, '~/Desktop/socrat')
from _LIB_ import network

class MACCS:
    default_mac       = None
    new_mac           = None
    current_mac       = None
    network_interface = None
    
    def __init__(self, default_mac, network_interface):
        self.default_mac       = default_mac
        self.network_interface = network_interface
        MACCS.maccs_process(self)
        
    def maccs_process(self):
        self.new_mac = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCS\033[0m}:MAC='))
        FNULL = open(os.devnull, 'w')
        self.current_mac = network.NW.get_mac_address(self.network_interface)
        
        #comnd = 'service networking stop'
        #subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        comnd = 'macchanger --mac='+str(self.new_mac)+' '+str(self.network_interface)
        subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        #comnd = 'service networking start'
        #subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

        if(network.NW.get_mac_address(self.network_interface) == self.new_mac):
            print('[\033[92m+\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_mac)+') -> ['+str(self.new_mac)+'][\033[92mSUCCESS\033[0m]')
        else:
            print('[\033[91m-\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_mac)+') -> ['+str(self.new_mac)+'][\033[91mUNSUCCESS\033[0m]')
    
    def __del__(self):
        del self
        
