# -*- coding: utf-8 -*-

# __title__ = '02-递归-汉诺塔.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.08.31'


# 汉诺塔：n表示盘子，a，b，c表示柱子,顺序意义是，盘子从 a 经过 b 到c
def hanoi(n,a,b,c):
	if n > 0:
		hanoi(n-1,a,c,b)
		print("moving from %s to %s"%(a,c))
		hanoi(n-1,b,a,c)


hanoi(100,"A","B","C")








