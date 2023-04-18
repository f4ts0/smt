import os
import sys

#input validation

while True:
    smt_val = input("Please select SMT on or off': ")
    if smt_val == 'on':
        break
    elif smt_val == 'off':
        break
    else:
        print("Wrong input, please try again.")

print("SMT config selected:", smt_val)

#exec command in python 
command = f'echo {smt_val} > /sys/devices/system/cpu/smt/control'
os.popen(command,'r',1)
