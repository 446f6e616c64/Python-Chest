#!/usr/bin/env python3

"""
This script is designed to verify if the operating
system is Ubuntu 18.04 using Python3.
@446f6e616c64
last updated: 2/22/2019
"""

import os
import platform

a = 'Ubuntu'
b = '18.04'
c = platform.linux_distribution()
d = c[0]
e = c[1]

print(a) # Ubuntu
print(b) # 18.04
print(c) # the entire string
print(d) # Ubuntu from string
print(e) # 18.04 from string


if d != a:
    # os.system('clear')
    print('requires Ubuntu')

else:
    if e != b:
        # os.system('clear')
        print('requires 18.04')
    else:
        # os.system('clear')
        print('correct OS')
