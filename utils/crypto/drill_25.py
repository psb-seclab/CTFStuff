import hashlib


pswd_ok = 'pswd_ok.txt'
pswd_better = 'pswd_better.txt'
pswd_strong = 'pswd_strong.txt'



def gen_hash():
	hash_str = ""
	fi = open(pswd_ok, 'rt')
	for row in fi:
		row = row.replace('\n', '')
		hash_str += hashlib.md5(row).hexdigest() + '\n'

	fo = open('md5_'+pswd_ok, 'wt')
	fo.write(hash_str)

	fi.close()
	fo.close()
	pass


if __name__ == '__main__':
	gen_hash()
	pass
