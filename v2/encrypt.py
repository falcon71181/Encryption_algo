from bs64 import bs64encode
from secret import DATA, KEY, NONCE
from chacha20 import encryptmsg

def encrypt(data):
    enmsg = []
    for char in data :
        char = ( 15 * char ) % 254
        enmsg.append(char)
    result = bytes(enmsg)
    return result

result = encryptmsg(DATA,KEY,NONCE)
result = encrypt(result).hex()
result = bs64encode(result)
result = result.decode() # to convert bytes into string
print(result)

with open('msg.env','w') as f:
    f.write(result)