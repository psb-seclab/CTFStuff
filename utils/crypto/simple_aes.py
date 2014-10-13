from Crypto.Cipher import AES

key = '0123456789abcdef' # a multiple of 16
# '\x00' is treated as bytes rather than str
IV = 16 * '\x00'           
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
