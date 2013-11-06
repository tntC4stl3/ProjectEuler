# coding:utf-8
# author:tntC4stl3

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt

def d(num):
	divisors = set()
	divisors.add(1)
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			divisors.add(i)
			divisors.add(num / i)
	return sum(list(divisors))

result = []
for a in range(1, 10001):
	b = d(a)
	if a == d(b) and a != b:
		result.append(a)

print sum(result)