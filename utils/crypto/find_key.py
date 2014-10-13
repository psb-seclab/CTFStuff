from Crypto.Cipher import AES

# you may modify this script to accomplish drill 21
# make sure you pad the key using '\x20' to make it 16 bytes

#word = 10*'a' # this is read from the word list!
word = 'median'
padsize = 16 - len(word) # this is determined by the word size
key = word + padsize*'\x20'
IV = 16 * '\x00'           
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

# !!!
# The text has to be padded as well sincie it is not a multiple of 16!!
# we use the PKCS5 padding scheme
# the length of plain text is 21, to make it 32 = 2*16, we need to pad 11 bytes
# in hex 11 = 0b
text = "This is a top secret." + 11*'\x0b'

print text
ciphertext = encryptor.encrypt(text)

print ciphertext.encode('hex')

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

print plain
