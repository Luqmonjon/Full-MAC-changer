import subprocess
interface=input("Interface> ")
new_mac=input("mac> ")
"""
subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+ interface + " hw ether "+new_mac,  shell=True)
subprocess.call("ifconfig " + interface +" up", shell=True)
"""
# Yuqoridagi scriptda agar foydalanuvchi boshqa qiymat kiritib yuborsa noto'g'ri buyruq
# ishga tushadi, shuning uchun buni ozgina o'zgartiramiz

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])