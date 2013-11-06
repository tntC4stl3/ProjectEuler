# coding:utf-8
# author:tntC4stl3

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from datetime import datetime
from math import sqrt

def isPrime1(num):
	'''方法一：从2到num/2，看能否被num整除，不能，则说明是素数'''
	for i in range(2, num/2+1):
		if num % i == 0:
			return False
	return True

def isPrime2(num):
	'''方法二：检查从2到sqrt（n）之间的数就可以了，因为如果一个数有因子的话，那么它必定有一个因子不大于该数的平方根。'''
	for i in range(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__':
	num = 2
	count = 0

	start = datetime.now()
	while True:
		if isPrime1(num):
			count += 1
		if count == 10001: # if is the 10001st prime, quit loop
			break
		num += 1
	end = datetime.now()
	print num
	print "isPrime1(num) spend %s." % (end - start)

	num = 2
	count = 0

	start = datetime.now()
	while True:
		if isPrime2(num):
			count += 1
		if count == 10001: # if is the 10001st prime, quit loop
			break
		num += 1
	end = datetime.now()
	print num
	print "isPrime2(num) spend %s." % (end - start)