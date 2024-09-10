#!/usr/bin/env python
import subprocess
import optparse
def get_args():

    reader=optparse.OptionParser()
    reader.add_option("-i","--interface",dest="interface",help="Interface name")
    reader.add_option("-m","--mac",dest="new_mac",help="New Mac address")
    
    return reader.parse_args()
def changer_mac(interface,new_mac):

    print("Changing mac addres to ",new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])



# interface=value.interface
# new_mac=value.new_mac      endi bizga bu ikki qator kerak emas
(value,key)=get_args()
changer_mac(value.interface,value.new_mac)#funksiyani chaqirdik
