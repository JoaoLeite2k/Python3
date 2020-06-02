import base64

count = 0

while count == 0:
    print('1. Crypt')
    print('2. Decrypt')
    print('0. Exit')
    resp = int(input('> '))
    if resp == 1:
        print('Message to encode: ', end='')
        message = str(input(' '))
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(base64_message)
    if resp == 2:
        print('Message to decode: ', end='')
        message_to_decodoe = str(input(' '))
        base64_message = message_to_decodoe
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print('Decoded message: ',end='')
        print(message)
    if resp == 0:
        count = count + 1




