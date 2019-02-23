#!/usr/bin/env python3

'''
This script is designed to verify that the script
has System level privileges using Python3.
@446f6e616c64 - 2/22/2019
version 1.0
'''

import os

try:
    is_admin = os.getuid()
except AttributeError:
    is_admin = ctyoes.wind11.shell32.IsUserAnAdmin()

if is_admin != 0:
    os.system('clear')
    print('Error - Script Requires System Level Privileges')
    exit()
else:
    print('Correct Privileges')
