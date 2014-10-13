from Crypto.Cipher import AES

# you may modify this script to accomplish drill 21
# make sure you pad the key using '\x20' to make it 16 bytes

IV = 16 * '\x00'           
mode = AES.MODE_CBC

# !!!
# The text has to be padded as well sincie it is not a multiple of 16!!
# we use the PKCS5 padding scheme
# the length of plain text is 21, to make it 32 = 2*16, we need to pad 11 bytes
# in hex 11 = 0b
text = "This is a top secret." + 11*'\x0b'
target = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"

with open('words.txt', 'r') as fin:
	word_list = fin.read().split('\n')
	#print len(word_list)
	for word in word_list:
		if len(word) < 17:
			padsize = 16 - len(word)
			tmpkey = word
			word += padsize*'\x20'
			encryptor = AES.new(word, mode, IV=IV)
			ciphertext = encryptor.encrypt(text)
			if target == ciphertext.encode('hex'):
				print "got the key:\t" + tmpkey
			#if tmpkey == 'median':
			#	print IV
			#	print text
			#	print ciphertext.encode('hex')
			#	print target

