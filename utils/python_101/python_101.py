# -*- coding: utf-8 -*-

def test_control_flow():
	return

def test_dictionary():
	return

def test_list():
	# items in list can be heterogeneous
	a = ['spam', 'eggs', 100, 1234, 2*2]
	b = [1, 2 ,3, 4]
	c = range(12)
	print a
	print b
	print c
	# access list elements
	print a[0]
	return

def test_str():
	"""play with string"""
	str_1 = "hacking is fun"
	print str_1 + 16*'a'
	print str_1 + 16*'\x61'
	print len(str_1)
	# take a substring
	# str[left:right]
	print str_1[:]
	print str_1[:5]
	# do not modify char in a string
	#str_1[0] = 'H'
	# print the last char
	print str_1[-1]

	return

def test_var():
	a = 5
	b = 1.2
	c = 0xdeadbeef
	d = u'\xde\xad\xbe\xef'
	e = 8 * '\x00'
	f = 'abcd'
	ff = '\x61\x62\x63\x64'
	kk = u'你好'
	g = True
	h = False
	print not g
	print a, b, c
	print a+b
	print type(c)
	print type(a)
	print type(d)
	print hex(c)
	print f, ff
	print kk.encode('utf-8')
	print d.encode('utf-8')
	return


if __name__ == "__main__":
    #test_var()
    #test_str()
    test_list()


