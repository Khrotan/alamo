__author__ = 'khrotan'
import subprocess
import os

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

partition="/dev/sdc2"
source="/home/khrotan/Masaüstü/pardus_kurumsal_2013_gnome_64bit_tr.iso"
output=cmd_output(["cp", source, partition])
output=str(output)
os.system("sync")