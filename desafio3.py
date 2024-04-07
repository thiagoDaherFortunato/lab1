import string
import random
import collections

def encrypt_vigenere(plaintext, key):
    """
    Encrypts the plaintext using the Vigenere cipher with the given key.
    """
    ciphertext = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    """
    Decrypts the ciphertext encrypted with the Vigenere cipher using the given key.
    """
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

# Example usage:


def getGroup(text,numGroups,groupStart):
    group = ''
    for i in range(groupStart, len(text),numGroups):
        group += text[i]
    return group
def splitGroup(text,numGroups):
    groups = []
    for i in range(0,numGroups):
        groups.append(getGroup(text,numGroups,i))
    return groups;

def frequenAtakVing(text,keylen,teste=0):
    groups = splitGroup(text,keylen)
    print("groups", groups)
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ""
    decode = ""

    for group in groups:
        freq = collections.Counter(group).most_common()
        print("max",freq)

        for shift in range(teste,len(freq)):
            max(freq)
            decode = decrypt_vigenere(group,freq[shift][-2])
            coded = encrypt_vigenere(decode,freq[shift][-2])
            if coded==group :
                key += freq[shift][-2]
                break
    return key;



key1 = frequenAtakVing("Coqebkxmk ow Mywzedkmky 2024/1", 1)
print("key",key1)
print(decrypt_vigenere("Coqebkxmk ow Mywzedkmky 2024/1",key1))
print('--------------------------------------')



'''pt_letter_frequency = {
        'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02,
        'g': 1.30, 'h': 1.28, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78,
        'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53,
        's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21,
        'y': 0.01, 'z': 0.47
}

    # Função para calcular o índice de coincidência de um segmento
''''''
portuguese_frequencies = {
    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02,
    'g': 1.30, 'h': 0.40, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78,
    'm': 4.74, 'n': 4.63, 'o': 9.50, 'p': 2.40, 'q': 1.21, 'r': 6.53,
    's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21,
    'y': 0.01, 'z': 0.47
}
def index_of_coincidence(segment):
    segment_length = len(segment)
    freq = collections.Counter(segment)
    ic = sum((freq[letter] * (freq[letter] - 1)) / (segment_length * (segment_length - 1)) for letter in freq)
    return ic'''







