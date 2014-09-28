__author__ = 'khrotan'
import subprocess
from subprocess import PIPE
def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

file="/home/khrotan/Masaüstü/mamama.iso"
output = cmd_output(["stat",file])
output=str(output)
a=output.find("Size:")
output=output[a+6:]
b=output.find(" ")
output=output[:b]
print(output)