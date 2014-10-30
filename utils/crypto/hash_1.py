import hashlib

if __name__ == '__main__':
	P = "welcome to cmpsc 497C"

	md5_hash = hashlib.md5(P).hexdigest()
	sha_hash = hashlib.sha1(P).hexdigest()
	sha224_hash = hashlib.sha224(P).hexdigest()
	sha256_hash = hashlib.sha256(P).hexdigest()
	sha384_hash = hashlib.sha384(P).hexdigest()
	sha512_hash = hashlib.sha512(P).hexdigest()

	print md5_hash, len(md5_hash)
	print sha_hash, len(sha_hash)
	print sha224_hash, len(sha224_hash)
	print sha256_hash, len(sha256_hash)
	print sha384_hash, len(sha384_hash)
	print sha512_hash, len(sha512_hash)

