#!/usr/bin/python3

'''
This script is designed to download and install system updates/upgrades for
a Debian based Operating System. This was tested on Ubuntu 18.04
@446f6e616c64 - 23FEB2019
'''

import os

os.system('sudo apt-get update')
os.system('sudo apt-get upgrade -y')
os.system('sudo apt-get dist-upgrade -y')
# os.system('sudo do-release-upgrade')
