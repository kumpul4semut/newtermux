# -*- coding: utf-8 -*-
import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

os.system("clear")
semut=(gt+"""
 #####  ####### #     # #     # ####### 
#     # #       ##   ## #     #    #    
#       #       # # # # #     #    #    
 #####  #####   #  #  # #     #    #    
      # #       #     # #     #    #    
#     # #       #     # #     #    #    
 #####  ####### #     #  #####     #    
 =================================
""")
slowprints(semut)
print(gt+"")
input('\n   Press enter to continue...')
sleep(2)
slowprints("   [!] Making Termux Properties directory...")
sleep(4)
try:
      os.mkdir("/data/data/com.termux/files/home/.termux")
except:
      pass
slowprints("   [!] Success Making Termux Properties directory!")
sleep(3)
slowprints("   [!] Making Setup file...")
sleep(1)

shortcutkey = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
script = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
script.write(shortcutkey)
script.close()
sleep(1)
slowprints("   [!] Success Making Setup file...")
sleep(2)
slowprints("\n   [!] Setting up setup file...")
sleep(2)
os.system("termux-reload-settings")
slowprints("   [!] Successfully !! Making Termux Shortcut Key, Terimakasih sudah memakai script ini untuk membantu anda :)")
os.system("rm -f key.py")
os.system('exit')
