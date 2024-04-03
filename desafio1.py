# XOR is a cheap way to encrypt data with a password.
# Any data can be encrypted using XOR as shown in this Python example...

from os import urandom

def genkey(length: int) -> bytes:
    """8-bit key."""
    return str.encode(''.join([chr(ord('A'))*length]))

def xor_strings(s, t) -> bytes:
    """Concate xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
    else:
        print('else')
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


message = 'This is the unencrypted message!'
print('Message:   ', message)

key = genkey(len(message))
print('Key:       ', key)

cipherText = xor_strings(message.encode('utf8'), key)
print('cipherText:', cipherText)
print('cipherText:', cipherText)
print('decrypted:', xor_strings(cipherText, key).decode('utf8'))
print('key ',  (key==xor_strings(cipherText, message.encode('utf8'))))
"""
#resolução desafio 1
test_str = message
res = ''.join(format(i,'b')for i in bytearray(test_str, encoding = 'utf-8'))
print(str (message.encode('utf8')))
key = ''.join(format(i,'b')for i in bytearray(str(key), encoding = 'utf-8'))
print(str(key).encode('utf8'))
print(xor_strings(message.encode('utf8'),str(key).encode('utf8')))
print(xor_strings(message,cipherText))
print(xor_strings(key2,cipherText))
#print(xor_strings(message,xor_strings(message.encode('utf8'),str(key).encode('utf8'))))
#print(xor_strings(res , key2))
"""

#cipherTest= str("rDFTS@OB@\x01DL\x01bNLQTU@B@N\x01\x13\x11\x13\x15\x0e\x10").encode('utf8')
cipherTest= "'rDFTS@OB@\x01DL\x01bNLQTU@B@N\x01\x13\x11\x13\x15\x0e\x10'"
discoverkey = xor_strings(message.encode('utf8'), cipherTest.encode('utf8'))
print('discoverkey',discoverkey.decode)
print('cipherTes1t:', cipherTest.encode('utf8'))
print('cipherTest2:', xor_strings(message, discoverkey))
print('discoverkey',discoverkey)
print('discoverkey',discoverkey)
print('decrypted1:', message)
print("decrypted2:", xor_strings(cipherTest, discoverkey).decode('utf8'))
print("decrypted2:", xor_strings(cipherTest, discoverkey).decode('utf8'))
print("teste cipherTest e message",(cipherTest==xor_strings(message, discoverkey).decode('utf8')))
print("teste",xor_strings(cipherTest, discoverkey).decode('utf8') == message)

# Verify
if xor_strings(cipherText, key).decode('utf8') == message:
    print('Unit test passed')
else:
    print('Unit test failed')