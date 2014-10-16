# -*- coding: utf-8 -*-

def test_db():
	
	return

def test_network():
	
	return


def test_class():
	return


def test_function():
	return

def test_io():

	return

def test_loops():
	return

def test_control_flow():
	# get input from keyboard
	x = int(raw_input("Please enter #:"))
	if x < 0:
	  x = 0
	  print 'Negative changed to zero'
	elif x == 0:
	  print 'Zero'
	elif x == 1:
	  print 'Single'
	else:
	  print 'More'
	return


def test_dictionary():
	pass

def test_list():
	# items are ordered
	# items in list can be heterogeneous
	a = ['spam', 'eggs', 100, 1234, 2*2]
	b = [1, 2 ,3, 4]
	c = range(12)
	print a
	print b
	print c
	# access list elements
	print a[0]
	for num in b:
		num += 1
	print b
	for i in range(len(b)):
		b[i] += 1
	print b
	# loop through a list
	for item in a:
		print item
	# add a new item to a list
	b.append(6)
	print b
	# delete a item based on location
	del b[0]
	del b[-1]
	print b
	#check membership
	if 'spam' in a:
		print 'got it'
	else:
		print 'spam is not in list a'
	# lists cancatenation
	d = a + b + c
	print d
	# list repetiion
	print 2*a
	# nested list
	print max(a)
	a.sort()
	print a
	a.reverse()
	print a
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
	# check a string's hex
	print str_1.encode('hex')
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
	j = 0x61
	print not g
	print a, b, c
	print a+b
	print type(c)
	print type(a)
	print type(d)
	print hex(c)
	print f, ff
	print chr(j)
	print kk.encode('utf-8')
	print d.encode('utf-8')
	return


if __name__ == "__main__":
    #test_var()
    #test_str()
    #test_list()
    #test_dictionary()
    test_control_flow()


