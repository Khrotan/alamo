__author__ = 'khrotan'

import subprocess

partition = "/dev/sdb3"

destination = "/home/khrotan/Masaüstü/mamama.iso"

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

output = cmd_output(["dd", "if=%s" %partition,"of=%s" %destination])
output = str(output)
first=output.find("(")
second=output.find(")")
mb=output[first+1:second]
output=output[2:]
print(output)