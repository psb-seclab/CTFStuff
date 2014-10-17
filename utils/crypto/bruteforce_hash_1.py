import string
from hashlib import sha256

check = '61e18627ead3caaf56c89140e11533491ea3cc7b405d3e4d95bba333860c0acc'
cnt = 0

def brutefoce_flag():
	global cnt
	for a in string.hexdigits:
		for b in string.hexdigits:
			for c in string.hexdigits:
				for d in string.hexdigits:
					cnt += 1
					# construct the potential solution
					flag = 'ASIS_b6b'+a+'244608c2'+b+'c2e869cb56'+c+'67b64'+d+'b1'
					if sha256(sha256(flag).hexdigest()).hexdigest() == check:
						print 'got the flag = ', flag
						return cnt

if __name__ == "__main__":
	count = brutefoce_flag()
	print 'tried %d times'%(count)
