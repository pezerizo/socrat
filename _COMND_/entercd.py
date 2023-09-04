from datetime import datetime

class COMMAND:
    def main_menu_get_comnd():
        while(1):
            try:
                comnd = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU\033[0m}: '))
                if str(comnd).isalnum():
                    return str(comnd)
            except:
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(comnd)+'\'')
    def privacy_menu_get_comnd():
        while(1):
            try:
                comnd = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY\033[0m}: '))
                if str(comnd).isalnum():
                    return str(comnd)
            except:
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/PRIVACY\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(comnd)+'\'')
    def scan_menu_get_comnd():
        while(1):
            try:
                comnd = str(input('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN\033[0m}: '))
                if str(comnd).isalnum():
                    return str(comnd)
            except:
                print('['+datetime.now().strftime('%H:%M:%S')+'][\033[1m\033[94mSYSTEM\033[0m]{\033[4mMENU/SCAN\033[0m>\033[91mERROR\033[0m}: unknow command \''+str(comnd)+'\'')
        
        
