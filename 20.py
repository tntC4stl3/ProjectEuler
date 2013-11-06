# coding:utf-8
# author:tntC4stl3

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# 计算100！
num = 1
for i in xrange(1,101):
	num *= i

count = 0
for i in str(num):
	count += int(i)

print count