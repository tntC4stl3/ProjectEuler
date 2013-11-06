# coding:utf-8
# author:tntC4stl3

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

letters = {
	1 : 3, # one
	2 : 3, # two
	3 : 5, # three
	4 : 4, # four
	5 : 4, # five
	6 : 3, # six
	7 : 5, # seven
	8 : 5, # eight
	9 : 4, # nine
	10 : 3, # ten
	11 : 6, # eleven
	12 : 6, # twelve
	13 : 8, # thirteen
	14 : 8, # fourteen
	15 : 7, # fifteen
	16 : 7, # sixteen
	17 : 9, # seventeen
	18 : 8, # eighteen
	19 : 8, # nineteen
	20 : 6, # twenty
	30 : 6, # thirty
	40 : 5, # forty
	50 : 5, # fifty
	60 : 5, # sixty
	70 : 7, # seventy
	80 : 6, # eighty
	90 : 6 # ninety
}

count = 0 # 用来统计letter数量
test = 0
for i in xrange(1, 1001):
	dd = i
	if i == 1000:
		count += 11 # one thousand
		print dd, count - test
		break
	num = i / 100 # 得到百位数字
	if num != 0: # num > 100
		count += letters[num]
		count += 7 # hundred
		if i % 100 != 0:
			count += 3 # and
		else:
			print dd, count - test
			test = count
			continue

	i %= 100

	if letters.has_key(i): # 特殊情况
		count += letters[i]
		print dd, count - test
		test = count
		continue

	num = i / 10
	if num != 0: # 不在特殊情况列，则可能是73,45之之类的数
		count += letters[num*10]
		i = i % 10
		count += letters[i]
		print dd, count - test
		test = count

print count