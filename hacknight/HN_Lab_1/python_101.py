# -*- coding: utf-8 -*-

#import my_math
from my_math import factorial
import os
#import my_math


def test_db():
	
	return

def test_network():
	
	return

def test_exception():
	# opening file failed
	try:
		fi = open("testfile", 'r')
   		fh = open("testfile", "w")
   		fh.write("This is my test file for exception handling!!")
	except IOError:
   		print "Error: can\'t find file or read data"
	else:
   		print fi.read()
   		print "Written content in the file successfully"
   		fh.close()
   		fi.close()
	return

def test_module():
	print '10! = %d'%(factorial(10))
	return

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      	self.name = name
      	self.salary = salary
      	Employee.empCount += 1
   
   def displayCount(self):
     	print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      	print "Name : ", self.name,  ", Salary: ", self.salary



def test_class():
	"This would create first object of Employee class"
	emp1 = Employee("Zara", 2000)
	"This would create second object of Employee class"
	emp2 = Employee("Manni", 5000)
	emp1.displayEmployee()
	emp2.displayEmployee()
	print "Total Employee %d" % Employee.empCount
	print emp1.empCount
	# inheritence
	# overiding
	# operator overloading

	return


def fib_1(n):
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while b < n:
		print b
		a, b = b, a+b
	return

cnt = 0
fib_tmp = {}# make fib faster
def fib_2(n):
	"""return the nth fib num"""
	global cnt
	cnt += 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		return fib_2(n-1) + fib_2(n-2)
	else:
		print 'invalid input'
		return None

def simple_func(a, b, c):
	return a + b + c**3

def test_function():
	print simple_func(1, 2, 3)
	fib_1(100)
	print fib_2(5)
	print 'fib_2 is called %d times'%(cnt)
	return

def test_generator():
	l1 = range(100)
	print l1
	# the first 100 odd numbers
	l2 = [2*x+1 for x in range(100)]
	print l2
	# gen a dict
	# gen a ascii code table
	dict1 = {x:chr(x) for x in range(128)}
	print dict1
	# gen a 10*10 array
	l3 = [[10*x+y for y in range(10)] for x in range(10)]
	print l3
	# cross product
	vec1 = [2, 4, 6]
	vec2 = [1, 3, 5]
	cross_product = [x*y for x in vec1 for y in vec2]
	print cross_product
	# using if
	vec_if = [x for x in l1 if x % 7 == 0]
	print vec_if
	print len(vec_if)
	return


def test_file_io():
	# write to a file
	fo = open('testfile', 'wt')
	for x in range(20):
		fo.write(str(x) + ',')
	fo.close()
	# read from a file
	fi = open('testfile', 'rt')
	# read as much as possible at one time!
	contents = fi.read()
	print contents
	list_num = contents.split(',')
	# read a line at a time
	# reset file obj position
	fi.seek(0)
	for line in fi:
		print line
	fi.seek(10)
	print fi.read(10)
	# tell the current position
	print fi.tell()
	fi.close()
	# create a dir
	import os
	os.mkdir("test_dir")
	# 
	return


def test_io():
	# print function
	a = ['hello', 'this is fun', 'I love wargames']
	for item in a:
		print item, len(item)
	# get input from keyboard
	# raw_input, get a line of input from keyboard as string
	x = str(raw_input("enter something:"))
	print x
	# input
	x = input("input your python expression: ")
	print x
	return

def test_loops():
	# for loops, break, continue
	# problem: check prime
	n = 23
	prime = True
	for x in range(2, n):
		if n % x == 0:
			print '%d is not a prime since it has a factor %d'%(n, x)
			prime = False
			break
	if prime:
		print '%d is a prime'%(n)
	# using while loop do the same
	prime = True
	x = 2
	while x < n:
		if n % x == 0:
			print '%d is not a prime since it has a factor %d'%(n, x)
			prime = False
			break
		x += 1
	if prime:
		print '%d is a prime'%(n)
	
	# do while?
	n = 1
	while True:
		if n < 10:
			print n
		n += 1
	
	return

def test_control_flow():
	# get input from keyboard
	#x = int(raw_input("Please enter #:"))
	x = 5
	if x < 0:
		x = 0
	  	print 'Negative changed to zero'
	elif x == 0:
	  	print 'Zero'
	elif x == 1:
	  	print 'Single'
	else:
	  	print 'More'
	# no case statement

	return


def test_dictionary():
	# create a dictionary
	dict_1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
	print dict_1
	dict_2 = {x:x*'a' for x in range(10)}
	print dict_2
	# add a new entry
	dict_1['newguy'] = '2323'
	print dict_1
	# del a entry
	del dict_1['Beth']
	print dict_1
	# check for existance
	print dict_1.has_key('Beth')
	print 'Beth' in dict_1
	print 'Alice' in dict_1
	# update dict
	print dict_1['Alice']
	dict_1['Alice'] = '323232'
	print dict_1['Alice']
	# no duplicates!
	# make a copy
	copy_dict_1 = dict_1.copy()
	print copy_dict_1
	
	# clear the dict
	dict_1.clear()
	print dict_1
	return

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
	# index function
	print index('spam')
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
	# copy a string
	str_2 = str_1
	str_3 = str_1[:-1]
	print id(str_2) == id(str_1)
	print id(str_3) == id(str_1)
	print str_1
	print str_2
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
	# the id function

	# global var
	return


if __name__ == "__main__":
    #test_var()
    test_str()
    #test_list()
    #test_dictionary()
    #test_control_flow()
    #test_loops()
    #test_function()
    #test_generator()
    #test_module()
    #test_io()
    #test_file_io()
    #test_class()
    #test_exception()
    
