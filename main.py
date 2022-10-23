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

def adb_swipe(xs, ys, xe, ye, time_milisec):
    adb_command='adb -s %s shell input swipe %s %s %s %s %s'%(id_device,xs,ys,xe,ye,time_milisec)   
    subprocess.call(adb_command)

def auto_start_up(account, password):
    print('Loging: %s'%account)
    #-----------------------------LOGIN----------------------------------
    # Click to text field acc78.2,313.2
    adb_click(78.2,313.2)
    time.sleep(1)
    adb_send_text(account)
    time.sleep(1)
    # Click to text field password 78.2,409.1
    adb_click(78.2,409.1)
    time.sleep(1)
    adb_send_text(password)
    time.sleep(1)
    # Click to checkbox
    adb_click(32.7,674.1)
    time.sleep(1)
    # Click to login button  265.1,815.5
    adb_click(265.1,815.5)
    time.sleep(3)


    # #--------------------------START-UP----------------------------------
    # # Click button start-up 263.4,484.7
    # adb_click(263.4, 484.7)
    # time.sleep(3)
    # #Click back button  31.0,67.8
    # adb_click(31.0,67.8)
    #--------------------------LOGOUT------------------------------------
    # Click button profile 483.1,909.3
    adb_click(483.1,909.3)
    time.sleep(1)
    # Cuộn chuột
    #TODO:
    adb_swipe(281.4,800,281.4,197.8,1000)
    time.sleep(1)

    # Click to setting button 168.4,819.2
    adb_click(168.4,819.2)
    time.sleep(1)

    # Click to logout button 96.2,202.8
    adb_click(96.2,202.8)
    time.sleep(1)

    # Click to logout button conf  261.8,852.0
    adb_click(261.8,852.0)
    time.sleep(1)
    print('Logout: %s'%account)


# 330.1,183.2 icon Cáttart

adb_click(330.1, 183.2)
time.sleep(10)

# Click button start-up 263.4,484.7
adb_click(263.4, 484.7)
time.sleep(3)

# Reading text
f = open(path_text_list_account, 'r')
lines = f.read().split('\n')
for line in lines:
    acc = line.split('|')
    auto_start_up(acc[1], password)
    print('Success %s' %acc[1])
