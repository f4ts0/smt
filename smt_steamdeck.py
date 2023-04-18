import os
import sys

while True:
    smt_val = input("Please select SMT on or off': ")
    if smt_val == 'on':
        break
    elif smt_val == 'off':
        break
    else:
        print("Wrong input, please try again.")

print("SMT config selected:", smt_val)

#EXEC LINUX COMMANDS FROM PYTHON
command = f'echo {smt_val} > igort'
      #command = 'echo %s > igort'.format(val)
os.popen(command,'r',1)
