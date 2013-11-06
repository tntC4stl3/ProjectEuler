# coding:utf-8
# author:tntC4stl3

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

a = 1
bFind = False
while a <= 333 and bFind == False:
	b = a
	while True:
		c = 1000 - a - b
		if c < b: # 需要满足 a < b < c
			break
		if pow(a, 2) + pow(b, 2) == pow(c, 2): # 满足 a^2 + b^2 = c^2，跳出循环
			print a, b, c
			print a*b*c
			bFind = True
			break
		b += 1
	a += 1