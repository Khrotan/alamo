__author__ = 'khrotan'

import subprocess
import os
from subprocess import PIPE

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]
partition="/dev/sdb2"

def format(partition):
    output = cmd_output(["mkdosfs","-F 32","-I",partition])
    output=str(output)
    if output.find("contains a mounted file system") != -1:
        print("Please be sure about your partition is unmounted!")
    elif output.find("Not enough clusters") != -1:
        print("Please be sure about partition that you've chosen has enough clusters.")
    else:
        print("Gratz! Your partition has been succesfully formatted.")