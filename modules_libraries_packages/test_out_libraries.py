import this
from random import random
import math
import os
import datetime
import builtins

#this is the python enhancement proposals
# PEP 20

print(random())


num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
# gives us remainder of the 2 values# 5 can't go into 1, so the remainder is 1print(f"Remainder from 1/5: {math.remainder(1, 5)}")

# returns our current working directoryworking_directory = os.getcwd()print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")

cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')
# change directory - must exist# os.chdir("<folder_name>")# make a new directoryos.mkdir("<folder_name>")

# gives us today'sdate
print(f"Today's date: {datetime.datetime.now()}")

for name in dir(builtins):
    if name[0].islower():
        print(name)