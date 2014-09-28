__author__ = 'khrotan'
import subprocess

destination="/home/khrotan/Masaüstü/barzo"

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
#  kwds.setdefault("shell",True)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]

#checking for ls command
outputls = cmd_output(["ls", destination])
outputls = str(outputls)
outputls = outputls[1:]

#checking for whether is it destination or not
outputdest = cmd_output(["file",destination])
outputdest = str(outputdest)
outputdest = outputdest[:-3]
a=outputdest.find(':')
outputdest = outputdest[a+2:]


def main():
    if outputdest == 'directory':
        if len(outputls) == 2:
            print("Your destination is empty :)")
    if len(outputls) != 2:
        print("Your destination is not empty! Please choose an empty one.")

main()