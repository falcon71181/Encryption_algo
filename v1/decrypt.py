def decrypt(data):
    msg = []
    for char in data:
        char = (char * 17) % 254
        msg.append(char)
    print(bytes(msg))
    return bytes(msg)

with open('msg.env','r') as f:
    data = bytes.fromhex(f.read())

result = decrypt(data)