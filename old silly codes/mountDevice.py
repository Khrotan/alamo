__author__ = 'khrotan'

import subprocess
import os

partition = "/dev/sdb3"

partitionName = partition[5:]

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

check = cmd_output(["file", "/media/%s" %partitionName]) #media klasoru icinde olup olmadigini kontrol
check = str(check)
if check.find("ERROR") != -1: #mnt klasoru icinde degilse klasor aciyoruz
    os.system("mkdir /media/"+partitionName) #There is a BUG over here

check = cmd_output(["mount", "%s"%partition, "/media/%s"%partitionName]) #partitioni actigimiz klasore mount ediyoruz
check = str(check)
if len(check) == 3:
    print("Your device has been mounted into system successfully!")
elif check[-6:-3]== "yok":
    print("There is no device in %s"%partition)
else:
    print("Your device is already mounted!")