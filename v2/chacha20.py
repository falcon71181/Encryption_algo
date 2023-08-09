import os
from Crypto.Cipher import ChaCha20

def encryptmsg(msg):
     key = b"1a8f27e09c3d6b541b4e3848ff7d4b8a"
     nonce = b"b93a8e91f6d240c5e9f13a7a"
     cipher = ChaCha20.new(key=key, nonce=nonce)
     env = cipher.encrypt(msg)
     return env

def decryptmsg(msg):
     key = b"1a8f27e09c3d6b541b4e3848ff7d4b8a"
     nonce = b"b93a8e91f6d240c5e9f13a7a"
     cipher = ChaCha20.new(key=key, nonce=nonce)
     plaintext = cipher.decrypt(msg)
     return plaintext