# coding:utf-8
# author:tntC4stl3

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

num = pow(2, 1000)
result = 0
for i in str(num):
	result += int(i)
print result

# 一行的写法
print sum([int(i) for i in str(pow(2, 1000))])