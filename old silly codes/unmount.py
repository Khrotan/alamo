__author__ = 'root'
import subprocess

partition = "/dev/sdb2"

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

output = cmd_output(["umount","-t vfat",partition])
output = str(output)

if len(output) == 3:
    print("Your device has been unmounted from system.")
else:
    print("Your device doesn't exist or already unmounted.")
#b'umount: /dev/sdb3: ba\xc4\x9flanmad\xc4\xb1\n'
#b''