#!/usr/bin/env python
import subprocess
import optparse
reader=optparse.OptionParser()
reader.add_option("-i","--interface",dest="interface",help="Interface name")
reader.add_option("-m","--mac",dest="new_mac",help="New Mac address")

(value,key)=reader.parse_args()
interface=value.interface
new_mac=value.new_mac
print("Changing mac addres to ",new_mac)
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])