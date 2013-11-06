# coding:utf-8
# author:tntC4stl3

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

d, n = 3, 600851475143
while (d * d < n):
    if n % d == 0: n /= d
    else: d += 2
print n