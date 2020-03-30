#!/usr/bin/python
# A Script that generates Private/Public Keypairs

from Crypto.PublicKey import RSA
key = RSA.generate(1024)
f = open("Student001_private.pem", "wb")
f.write(key.exportKey('PEM'))
f.close()

pubkey = key.publickey()
f = open("Student001_public.pem", "wb")
f.write(pubkey.exportKey('OpenSSH'))
f.close()
