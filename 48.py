# coding:utf-8
# author:tntC4stl3

'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

result = 0
for i in xrange(1,1001):
	result += pow(i, i)

print str(result)[-10:]