# coding:utf-8
# author:tntC4stl3

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# 最简单的方法是，从起点到终点，一共会有40个方向可以选择，从中选出20个即可
# 也就是 C(40, 20)

# 呃，这个递归太耗时了，成指数级增长了
def countPaths(i, j):
	if i == 0 or j == 0:
		return 1
	else:
		return countPaths(i-1, j) + countPaths(i, j-1)

print countPaths(19, 19)