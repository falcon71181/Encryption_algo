from bs64 import bs64decode
from chacha20 import decryptmsg
from secret import KEY, NONCE

def decrypt(data):
    msg = []
    for char in data:
        char = (char * 17) % 254 # a=15,b=17,c=254 {(15*17)-1} = c
        msg.append(char)
    return bytes(msg)

with open('msg.env','r') as f:
    data = f.read()
    data = bs64decode(data).decode()
    data = bytes.fromhex(data)

result = decryptmsg(decrypt(data),KEY,NONCE)
print(result)