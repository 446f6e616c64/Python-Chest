#!/usr/bin/env python3

"""
This script is designed to create a new user account with a given
password using Python3.
@446f6e616c64
last updated: 2/22/2019
"""

import os
import getpass
import hashlib

passwd = getpass.getpass('Password:')

# DES Method for Hashing Password - NOT SECURE
# cpass = crypt.crypt(passwd, 'f2')
# m = hashlib.md5()
salt = 'a7'

hash = hashlib.sha256(salt+passwd).encode('utf-8').hexdigest()

# os.system("useradd -m -p %s -s /bin/bash danny3" % (hash))
print(hash)
