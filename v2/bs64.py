import base64

def bs64encode(msg):
    msg_bytes = msg.encode("ascii")
    msg_enc = base64.b64encode(msg_bytes)
    return msg_enc

def bs64decode(enmsg):
    msg = base64.b64decode(enmsg)
    return msg
