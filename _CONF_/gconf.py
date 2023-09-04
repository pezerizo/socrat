class CONFIGFILE:
    def correct_info(info):
        correct_info = list(str(info))
        if correct_info[len(correct_info)-1] == '\n':
            del correct_info[len(info)-1]
            info = ''.join(correct_info)
        return info
    
    def getdata():
        __config      = open('_CONF_/socrat.conf')
        __config_data = __config.readlines()
        netmask           = None
        gateway           = None
        broadcast         = None
        default_mac       = None
        mac_change_type   = None
        network_interface = None
        time_change       = None
                        
        for i in range(len(__config_data)):
            line = list(__config_data[i])
            if line[0] == '#': pass
            else:
                data = __config_data[i].split('~')
                if data[0] == 'gateway':
                    gateway = data[1]
                    gateway = CONFIGFILE.correct_info(gateway)
                if data[0] == 'broadcast':
                    broadcast = data[1]
                    broadcast = CONFIGFILE.correct_info(broadcast)
                elif data[0] == 'netmask':
                    netmask = data[1]
                    netmask = CONFIGFILE.correct_info(netmask)
                elif data[0] == 'default_mac':
                    default_mac = data[1]
                    default_mac = CONFIGFILE.correct_info(default_mac)
                elif data[0] == 'mac_change_type':
                    mac_change_type = data[1]
                    mac_change_type = CONFIGFILE.correct_info(mac_change_type)
                elif data[0] == 'network_interface':
                    network_interface = data[1]
                    network_interface = CONFIGFILE.correct_info(network_interface)
                elif data[0] == 'time_change':
                    time_change = data[1]
                    time_change = CONFIGFILE.correct_info(time_change)    
                else: pass
        data_from_file = (default_mac,mac_change_type,network_interface,time_change,netmask,gateway,broadcast)
        return data_from_file
