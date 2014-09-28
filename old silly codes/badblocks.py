__author__ = 'khrotan'

import os
from subprocess import PIPE,Popen
import subprocess


def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

partition = "/dev/sdb3"

output = cmd_output(["badblocks", "-v", partition])
output = str(output)

a = output.find("bad blocks") #It needs to change according to new lines

if int(output[a-2]) == 0:
    print("Your partition looks well fine! There seems to be no bad blocks.")
else:
    print("There are %d bad blocks in your partition. Please contact with an administrator." %output[a-2])