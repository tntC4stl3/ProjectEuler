# coding:utf-8
# author:tntC4stl3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import sqrt

def isPrime(num):
	'''方法二：检查从2到sqrt（n）之间的数就可以了，因为如果一个数有因子的话，那么它必定有一个因子不大于该数的平方根。'''
	for i in range(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__':
	sum = 0
	for i in range(2, 2000001):
		if isPrime(i):
			sum += i
	print sum