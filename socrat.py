from _MENU_ import menu
from _COMND_ import entercd
from _PACKAGE_ import maccd, maccs, ipcs, ipcd, scanport
from _CONF_ import gconf
from _LIB_ import network

from subprocess import Popen
from threading import Thread
from datetime import datetime
import sys

class SOCRAT:
    data = None
    def __init__(self):
        print('~'*50)
        self.data = gconf.CONFIGFILE.getdata()
        menu.MENU.main_menu(network.NW.get_connection_status(self.data[2]))
        while(1):
            ___command = entercd.COMMAND.main_menu_get_comnd()
            if ___command == '1':
                SOCRAT.netw_priv_menu()
            elif ___command == '4':
                SOCRAT.netw_scan_menu()
            
            elif ___command == '97':
                print("["+datetime.now().strftime('%H:%M:%S')+"][\033[1m\033[94mSYSTEM\033[0m]{\033[4mINFO/MAC\033[0m}: "+str(network.NW.get_mac_address(self.data[2])))
                print("["+datetime.now().strftime('%H:%M:%S')+"][\033[1m\033[94mSYSTEM\033[0m]{\033[4mINFO/IPL\033[0m}: "+str(network.NW.get_local_ip(self.data[2])))
                
            elif ___command == '99':
                exit(0)
                
            else:
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(___command)+'\'')
            
    def netw_priv_menu():
        menu.MENU.privacy_menu()
        while(1):
            __command = entercd.COMMAND.privacy_menu_get_comnd()
            if __command == '1':
                data = gconf.CONFIGFILE.getdata()
                maccs.MACCS(data[0], data[2])
            
            elif __command == '2':
                data = gconf.CONFIGFILE.getdata()
                new_thread_maccd = Thread(target=maccd.MACCD, args=(data[0], data[1], data[2]))
                new_thread_maccd.start()
                new_thread_maccd.join()
                
            elif __command == '3':
                data = gconf.CONFIGFILE.getdata()
                ipcs.IPCS(data[2], data[4], data[5], data[6])

            
            elif __command == '99':
                SOCRAT()
                
            else: 
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(__command)+'\'')
    
    def netw_scan_menu():
        menu.MENU.scan_menu()
        while(1):
            __command = entercd.COMMAND.scan_menu_get_comnd()
            if __command == '1':
                data = gconf.CONFIGFILE.getdata()
                scanport.SCANPORT(data[2])

            
            elif __command == '99':
                SOCRAT()
                
            else: 
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(__command)+'\'')
if __name__ == '__main__':
    menu.MENU.logo()
    SOCRAT()
