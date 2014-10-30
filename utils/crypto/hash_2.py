import hashlib

filename = 'pswd_sample.txt'
pswd_ok = 'pswd_ok.txt'
pswd_better = 'pswd_better.txt'
pswd_strong = 'pswd_strong.txt'

str_ok = ""
str_better = ""
str_strong = ""

with open(filename, 'rt') as fi:
	for row in fi:
		pswd_list = row.split()
		str_ok += pswd_list[0] + '\n'
		str_better += pswd_list[1] + '\n'
		str_strong += pswd_list[2] + '\n'
		
fo_ok = open(pswd_ok, 'wt')
fo_better = open(pswd_better, 'wt')
fo_strong = open(pswd_strong, 'wt')

fo_ok.write(str_ok)
fo_better.write(str_better)
fo_strong.write(str_strong)
fo_ok.close()
fo_better.close()
fo_strong.close()
fi.close()
