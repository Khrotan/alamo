__author__ = "khrotan"

import subprocess
from subprocess import check_output
from subprocess import PIPE,Popen
from subprocess import os


def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

partition = "/dev/sdb2"

stdout = Popen("df | grep " + partition, shell=True, stdout=PIPE).stdout
output = stdout.read()
output=str(output)
a=output.find("%")
output=output[a+2:-3]
print(output)