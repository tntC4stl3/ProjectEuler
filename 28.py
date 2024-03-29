# coding:utf-8
# author:tntC4stl3

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# 1001 * 1001 共有 501圈
# 第n层的几个数之间相差是2n-2
result = 1
num = 1 # 从1开始
for i in xrange(2, 502):
	for j in range(4): # 每层4个数
		num += 2 * i - 2
		result += num
print result