from datetime import datetime
import subprocess,sys,socket,struct
import os
import fcntl
import random
import time
import sys
sys.path.insert(0, '~/Desktop/socrat')
from _LIB_ import network


class MACCD:
    default_mac       = None
    new_mac           = None
    current_mac       = None
    mac_change_type   = None
    network_interface = None
    time_change       = None
    
    def __init__(self, default_mac, mac_change_type,
                       network_interface):
        self.default_mac       = default_mac
        self.current_mac       = network.NW.get_mac_address(network_interface)
        self.mac_change_type   = mac_change_type
        self.network_interface = network_interface
        MACCD.maccd_process(self)
        
    def maccd_process(self):
        mac_symbols = '0123456789abcdef'
    
        __elements_mac_type    = self.mac_change_type.split(':')
        _elements_mac_type     = ''.join(__elements_mac_type)
        elements_mac_type      = list(_elements_mac_type)
        __elements_default_mac = self.default_mac.split(':')
        _elements_default_mac  = ''.join(__elements_default_mac)
        elements_default_mac   = list(_elements_default_mac)
        
        print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCD\033[0m}: Start')
        self.time_change = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCD\033[0m}:PAUSE='))
        self.change_mac_count = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCD\033[0m}:COUNT='))
        if str(self.time_change).isalnum() and str(self.change_mac_count).isalnum():
            counter   = 0
            success   = 0
            unsuccess = 0
            while(1):

                self.new_mac = ''
                for i in range(len(elements_mac_type)):
                    if elements_mac_type[i] == 'y':
                        self.new_mac = str(self.new_mac)+str(elements_default_mac[i])
                    elif elements_mac_type[i] == 'x':
                        new_element = random.choice(mac_symbols)
                        self.new_mac     = str(self.new_mac)+str(new_element)
                nm      = list(self.new_mac)
                self.new_mac = ''
                var     = 0
                for i in range(len(nm)):
                    var += 1
                    self.new_mac = str(self.new_mac)+str(nm[i])
                    if var == 2:
                        var = 0
                        if i+1 == len(nm):
                            pass
                        else:
                            self.new_mac = str(self.new_mac)+':'
                del var
                del nm
                        

                FNULL = open(os.devnull, 'w')
                subprocess.call('macchanger --mac='+str(self.new_mac)+' '+str(self.network_interface), shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
                if(self.current_mac != network.NW.get_mac_address(self.network_interface)):
                    print('[\033[92m+\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_mac)+') -> ['+str(self.new_mac)+'][\033[92mSUCCESS\033[0m]')
                    self.current_mac = self.new_mac
                    success+=1
                else:
                    print('[\033[91m-\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_mac)+') -> ['+str(self.new_mac)+'][\033[91mUNSUCCESS\033[0m]')
                    unsuccess+=1
                counter+=1
                if int(success) == int(self.change_mac_count):
                    print('['+datetime.now().strftime('%H:%M:%S')+'][\033[4mSUCCESS\033[0m]:\033[92m'+str(success)+'\033[0m/[\033[4mUNSUCCESS\033[0m]:\033[91m'+str(unsuccess)+'\033[0m/[\033[4mALL\033[0m]:\033[94m'+str(counter)+'\033[0m')
                    print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCD\033[0m}: Stop')
                    return 1
                time.sleep(int(self.time_change))
                
    def __del__(self):
        del self
