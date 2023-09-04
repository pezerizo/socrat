import socket
import fcntl
import struct
from datetime import datetime

class NW:
    def get_mac_address(iframe):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', bytes(iframe, 'utf-8')[:15]))
        return ':'.join('%02x' % b for b in info[18:24])
        
    def get_local_ip(ifname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,
                struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
                [20:24])
        except:
            print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m][\033[91mERROR\033[0m] No connections')

    def get_connection_status(ifname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
            [20:24])
            return True
        except:
            return False
