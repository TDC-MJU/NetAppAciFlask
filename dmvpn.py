import sys
import time
import paramiko
import subprocess
import os.path
import re
import threading


username = 'netmri'
password = 'N3t!mri2011'
ch3 = '10.222.241.53'
ps2 = '10.221.241.115'

ps2outl = ['route-map ToDMVPN permit 5','set community 65111:50']
ch3outl = ['route-map ToDMVPN permit 5','set community 65112:50']
inservice = ['no route-map ToDMVPN permit 5']

def ps2out ():

    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(ps2, username = username, password = password)
    connection = session.invoke_shell()	
    connection.send("terminal length 0\n")
    time.sleep(1)
    connection.send("config t\n")
    time.sleep(1)
    connection.send("\n")
    for line in ps2outl():
   	connection.send(line +'\n')
   	time.sleep(3)
        connection.send("wr mem\n")
        time.sleep(3)
    session.close()




def ch3out():
   
  session = paramiko.SSHClient()
  session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  session.connect(ps2, username = username, password = password)
  connection = session.invoke_shell()	
  connection.send("terminal length 0\n")
  time.sleep(1)
  connection.send("\n")
  for line in ch3outl():
      connection.send(line +'\n')
      time.sleep(3)
  session.close()


def ps2in ():


  session = paramiko.SSHClient()
  session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  session.connect(ps2, username = username, password = password)
  connection = session.invoke_shell() 
  connection.send("terminal length 0\n")
  time.sleep(1)
  connection.send("\n")
  connection.send("no", ch3outl + '\n')
  time.sleep(3)
  session.close()
  


def ch3in():
  print('CH3 has been executed')
  session = paramiko.SSHClient()
  session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  session.connect(ps2, username = username, password = password)
  connection = session.invoke_shell() 
  connection.send("terminal length 0\n")
  time.sleep(1)
  connection.send("\n")
  connection.send('no',ch3outl[0],'\n')
  time.sleep(3)
  session.close()


def dmvpn(dop, loc, sp):
    if (loc == 'Piscataway') and (sp == 'OutService'):
        ps2out()
    elif (loc == 'Piscataway') and (sp == 'InService'):
        ps2in()
    elif (loc == 'Chicago') and (sp == 'OutService'):
        ch3out()
    elif (loc == 'Chicago') and (sp == 'InService'):
        ch3in()

