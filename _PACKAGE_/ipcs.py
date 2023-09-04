from datetime import datetime
import subprocess,sys,socket,struct
import os
import fcntl
sys.path.insert(0, '~/Desktop/socrat')
from _LIB_ import network

class IPCS:
	netmask = None
	gateway = None
	broadcast = None
	network_interface = None
	current_ipl = None
	new_ipl = None

	def __init__(self, network_interface, netmask, gateway, broadcast):
		self.network_interface = network_interface
		self.netmask = netmask
		self.gateway = gateway
		self.broadcast = broadcast
		IPCS.ipcs_process(self)
		

	def ipcs_process(self):
	    print('netmask:',self.netmask,'gateway:',self.gateway,'broadcast:',self.broadcast)
	    self.new_ipl = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/IPCS\033[0m}:IPL='))
	    FNULL = open(os.devnull, 'w')
	    self.current_ipl = network.NW.get_local_ip(self.network_interface)
	    
	    comnd = 'ifconfig '+str(self.network_interface)+' down'
	    subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	    comnd = 'ifconfig '+str(self.network_interface)+' '+str(self.new_ipl)+' netmask '+str(self.netmask)
	    subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	    comnd = 'ifconfig '+str(self.network_interface)+' up'
	    subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	    
	    if network.NW.get_local_ip(self.network_interface) != self.current_ipl:
	        print('[\033[92m+\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_ipl)+') -> ['+str(self.new_ipl)+'][\033[92mSUCCESS\033[0m]')
	    else:
	        print('[\033[91m-\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_ipl)+') -> ['+str(self.new_ipl)+'][\033[91mUNSUCCESS\033[0m]')
