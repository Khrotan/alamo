__author__ = 'khrotan'

import os
from subprocess import PIPE,Popen
try:
    partition = "/dev/sdb"
    stdout = Popen("df | grep " + partition, shell=True, stdout=PIPE).stdout
    output = stdout.read()
    output = str(output)
    output=output[3:-3]
    ilkbosluksirasi=output.find(' ')

    print(output)
except:
    print("Your device is not mounted into the system!")
