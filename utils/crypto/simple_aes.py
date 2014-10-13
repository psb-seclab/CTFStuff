from Crypto.Cipher import AES

key = '0123456789abcdef'
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'j' * 64 + 'i' * 128
print text
ciphertext = encryptor.encrypt(text)

print ciphertext.encode('hex')

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

print plain

print len(plain)
print len(ciphertext)
