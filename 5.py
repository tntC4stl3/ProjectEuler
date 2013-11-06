# coding:utf-8
# author:tntC4stl3

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# 约去不必要的数，比如能被8整除，肯定能被2，4整除，能被9整除，肯定能被3整除
# 所以留下 11, 13, 14, 15, 16, 17, 18, 19, 20

result = 1
while True:
	print result
	for i in range(1, 21):
		if result % i != 0:
			break
	else:
		print result
		break
	result += 1