__author__ = 'khrotan'

import subprocess
from subprocess import PIPE,Popen
import os

file = "/home/khrotan/Masaüstü/pardus_kurumsal_2013_gnome_64bit_tr.iso"

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

file_type = cmd_output(["file", file])
file_type = str(file_type)

def checkBootable():
    if file_type.find("bootable") != -1:
        print("Gratz! Your ISO looks bootable :)")
    else:
        print("Sorry, the ISO that you've chosen doesn't seems like suitable.")

checkBootable()