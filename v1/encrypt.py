from secret import DATA

def encrypt(data):
    enmsg = []
    for char in data :
        char = ( 15 * char ) % 254
        enmsg.append(char)
    return bytes(enmsg)

result = encrypt(DATA).hex()
print(result)
with open('msg.env','w') as f:
    f.write(result)
