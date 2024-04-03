def xor_block(message_block: bytes, key: bytes) -> bytes:
    """XOR operation between a block of message and the key."""
    return bytes([a ^ b for a, b in zip(message_block, key)])

def encrypt(message: bytes, key: bytes) -> bytes:
    """Encrypt the message using XOR block cipher."""
    cipher_text = b''
    for i in range(0, len(message), 16):
        message_block = message[i:i+16]
        cipher_text += xor_block(message_block, key * (len(message_block) // len(key)))
    return cipher_text

def decrypt(cipher_text: bytes, key: bytes) -> bytes:
    """Decrypt the cipher text using XOR block cipher."""
    decrypted_text = b''
    for i in range(0, len(cipher_text), 16):
        cipher_block = cipher_text[i:i+16]
        decrypted_text += xor_block(cipher_block, key * (len(cipher_block) // len(key)))
    return decrypted_text


message = 'This is the unencrypted message!'
cipher = "b'\\x12'&73#/! b$/a\\x01./175#\"#.bsrsvns'"
key = xor_block(message.encode('utf16'),cipher.encode("utf16"))
print('Message:', message)
print('Messa16:', message.encode('utf16'))
print ('ciphers:', cipher)
print ('ciphe16:', cipher.encode('utf16'))
print('key :',key)
message2 =  xor_block(cipher.encode('utf16'),key)
print('messacd:' , message2)
print('messadc:' , message2.decode('utf16'))
print('ciphecd:' , xor_block(message2,key))
print('ciphedc:' , xor_block(message2,key))
cipher2 =  xor_block(message.encode('utf16'),key).decode('utf16')
print(cipher)
print(cipher2)

print('validação mensagem', (message2==message.encode('utf16')))
print('validação ciphe', (xor_block(message.encode('utf16'),key)==cipher))



#print(xor_block(message.encode('utf16'),cipher.encode("utf16")))
#print('decrypt', decrypt(cipher.encode('utf16'),key))


#print('encrypt', encrypt(str(message).encode('utf16'),key))
#print('encrypt', encrypt(cipher.encode('utf16'),key))

#print('encrypt', encrypt(message,key))
#print('encrypt', encrypt(cipher,key))