# coding:utf-8
# author:tntC4stl3

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

max_palindromic = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		tmp = i * j
		if tmp > max_palindromic and str(tmp) == str(tmp)[::-1]:
			max_palindromic = tmp

print max_palindromic