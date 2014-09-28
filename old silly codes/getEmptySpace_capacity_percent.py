__author__ = 'khrotan'

import os
from subprocess import PIPE,Popen
try:
    partition = "/dev/sdb3"
    stdout = Popen("df | grep " + partition, shell=True, stdout=PIPE).stdout
    output = stdout.read()
    output = str(output)
    print(output)
    print(output[59:]) #TOTALLY JUNK CODE
    output = output[59:-3]

    a=output.find(' ')
    capacity=output[:a]
    output = output[a:]

    while output[0] == ' ':
        output = output[1:]

    a=output.find(' ')
    usage=output[:a]
    output = output[a:]

    while output[0] == ' ':
        output = output[1:]

    a=output.find(' ')
    usage=output[:a]
    output = output[a:]

    while output[0] == ' ':
        output = output[1:]

    a=output.find(' ')
    usagePercent=output[:a]
    output = output[a:]

    while output[0] == ' ':
        output = output[1:]

    mountedPoint = output
    print(capacity)
    print(usagePercent)
    print(usage)
    print("Your partition has " + capacity + " total capacity and you're using " + usage + " of it. You're using " + usagePercent + " percent of it.")

except:
    print("Your device is not mounted into the system!")
