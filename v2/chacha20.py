import os
from Crypto.Cipher import ChaCha20

def encryptmsg(msg,key,nonce):
     cipher = ChaCha20.new(key=key, nonce=nonce)
     env = cipher.encrypt(msg)
     return env

def decryptmsg(msg,key,nonce):
     cipher = ChaCha20.new(key=key, nonce=nonce)
     plaintext = cipher.decrypt(msg)
     return plaintext
