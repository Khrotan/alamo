import subprocess
from subprocess import check_output,Popen, PIPE
import os

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

source = "/media/sdfsfd"
destination = "/home/khrotan/Masaüstü/barzo"

stdout = Popen("rsync -r -a " + source + " " + destination, shell=True, stdout=PIPE).stdout
output = stdout.read()
output = str(output)
print(output)