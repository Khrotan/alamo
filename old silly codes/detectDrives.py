__author__ = 'khrotan'

import os
from subprocess import Popen, PIPE

stdout = Popen("find /dev/disk/ -ls | grep /usb", shell=True, stdout=PIPE).stdout
output = stdout.read()
output = str(output)
devices = list()

output = output + ("\\n")

print(output[output.find("../../")+6:output.find("\\n")])

many = output.count("\\n")

def deviceAppend(output,devices):
    start = output.find("/usb-")
    end = output.find("->")
    devices.append(output[start+5:end-1])
    start = output.find("../../")
    end = output.find("\\n")
    devices.append(output[start+6:end])

for i in range(many):
    deviceAppend(output,devices)
    output = output[output.find("\\n")+1:]

print(devices[:-2])