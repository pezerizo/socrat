from datetime import datetime
import subprocess,os,fcntl,socket,struct,time,random
import sys
sys.path.insert(0, '~/Desktop/socrat')
from _LIB_ import network

class IPCD:
	netmask = None
	gateway = None
	broadcast = None
	network_interface = None
	current_ipl = None
	new_ipl = None
	time_change = None
	change_ipl_count = None

	def __init__(self, network_interface, netmask, gateway, broadcast):
		self.network_interface = network_interface
		self.netmask = netmask
		self.gateway = gateway
		self.broadcast = broadcast
		self.current_ipl = network.NW.get_local_ip(self.network_interface)
		IPCD.ipcd_process(self)
		
	def get_new_ipl(self, netmask, ipl_current):
	    octats_netmask   = netmask.split('.')
	    octats_ipl       = ipl_current.split('.')
	    new_ipl          = ''
	    available_octats = [0, 0, 0, 0]
	    for x in range(len(octats_netmask)):
	        if octats_netmask[x] == '255':
	            available_octats[x] = 0
	        else:
	            available_octats[x] = 1
	    octats_new = [0, 0, 0, 0]
	    for y in range(len(available_octats)):
	        if available_octats[y] == 1:
	            octats_new[y] = str(random.randint(2, 254))
	        else:
	            octats_new[y] = octats_ipl[y]
	            
	    new_ipl = '.'.join(octats_new)
	    print(new_ipl)
	    print(octats_new)
	    return new_ipl
            

	def ipcd_process(self):
	    print('netmask:',self.netmask,'gateway:',self.gateway,'broadcast:',self.broadcast)
	    self.time_change = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/IPCD\033[0m}:PAUSE='))
	    self.change_ipl_count = int(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/IPCD\033[0m}:COUNT='))
	    
	    success = 0
	    unsuccess = 0
	    counter = 0
	    
	    while(1):
	        
	        FNULL = open(os.devnull, 'w')
	        self.new_ipl = self.get_new_ipl(self.netmask, self.current_ipl)
	    
	        comnd = 'ifconfig '+str(self.network_interface)+' down'
	        subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	        time.sleep(4)
	        comnd = 'ifconfig '+str(self.network_interface)+' '+str(self.new_ipl)+' netmask '+str(self.netmask)
	        subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	        time.sleep(4)
	        comnd = 'ifconfig '+str(self.network_interface)+' up'
	        subprocess.call(comnd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
	        time.sleep(4)
	    
	        if self.current_ipl != network.NW.get_local_ip(self.network_interface):
	            print('[\033[92m+\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_ipl)+') -> ['+str(self.new_ipl)+'][\033[92mSUCCESS\033[0m]')
	            success+=1
	            self.current_ipl = self.new_ipl
	        else:
	            print('[\033[91m-\033[0m]['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]: ('+str(self.current_ipl)+') -> ['+str(self.new_ipl)+'][\033[91mUNSUCCESS\033[0m]')
	            unsuccess+=1
	        counter+=1
	        if int(success) == int(self.change_ipl_count):
                    print('['+datetime.now().strftime('%H:%M:%S')+'][\033[4mSUCCESS\033[0m]:\033[92m'+str(success)+'\033[0m/[\033[4mUNSUCCESS\033[0m]:\033[91m'+str(unsuccess)+'\033[0m/[\033[4mALL\033[0m]:\033[94m'+str(counter)+'\033[0m')
                    print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY/MACCD\033[0m}: Stop')
                    return 1
	        time.sleep(int(self.time_change))
