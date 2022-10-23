from importlib.resources import path
import time
import subprocess
id_device='emulator-5558'
password = '123123'
path_text_list_account='acc.txt'

def adb_click(coord_x,coord_y):
    adb_command='adb -s %s shell input tap %s %s'%(id_device,coord_x,coord_y)
    subprocess.call(adb_command)

def adb_send_text(text):
    adb_command='adb -s %s shell input text %s'%(id_device,text)
    subprocess.call(adb_command)

def auto_start_up(account, password):
    print('Loging: %s'%account)
    #-----------------------------LOGIN----------------------------------
    # Click to text field acc
    # Click to text field password
    # Click to login button 

    #--------------------------START-UP----------------------------------
    # Click button start-up 263.4,484.7
    adb_click(263.4, 484.7)
    #--------------------------LOGOUT------------------------------------
    # Click button profile 483.1,909.3
    adb_click(483.1,909.3)
    # Cuộn chuột
    #TODO:

    # Click to setting button 168.4,819.2
    adb_click(168.4,819.2)

    # Click to logout button 96.2,202.8
    adb_click(96.2,202.8)

    # Click to logout button conf  261.8,852.0
    adb_click(261.8,852.0)
    print('Logout: %s'%account)


# 330.1,183.2 icon Cáttart

adb_click(330.1, 183.2)

# Reading text
f = open(path_text_list_account, 'r')
lines = f.readline()
for line in lines:
    acc = line.split('|')
    auto_start_up(acc[0], password)
    print('Success %s' %acc[0])
