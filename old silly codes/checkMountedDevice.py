__author__ = 'root'

import subprocess
from subprocess import check_output

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

partition="/dev/sdb3"
output = check_output("mount")
output=str(output)
if output.find(partition) != -1:
    print("The partition %s is mounted." %partition)
else:
    print("The partition %s is NOT mounted." %partition)