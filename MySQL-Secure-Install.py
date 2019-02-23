#!/usr/bin/python3

'''
This script is designed to install MySQL, Log into the newly created database,
and then secure it automatically using the same MySQL commands used by the
mysql_secure_installation command.

import os

os.system('sudo apt-get install -y mysql-server')

# TODO: Automate the creation, running, and deletion of the .sql file to allow for the user to input password
os.system('mysql -sfu root < "mysql-secure-install.sql"')

print('done')
