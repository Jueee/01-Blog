'''
for循环需要预先设定好循环的次数(n)，然后执行隶属于for的语句n次。

基本构造是

for 元素 in 序列: 
    statement
'''
for a in [2,4,6,756,'qweqw',True]:
	print(a)

#range生成了一个iterator，要转换成list的类型。
print(type(range(10)))
print(list(range(10)))

for a in range(10):
	print(a**2)

'''
while的用法是

while 条件:
    statement
while会不停地循环执行隶属于它的语句，直到条件为假(False)
'''
i = 1
while i < 10:
	print(i)
	i = i + 2

'''
中断循环

continue   # 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作

break      # 停止执行整个循环
'''
for x in range(1,10):
	if x == 7:
		continue
	print(x)

for x in range(1,10):
	if x == 7:
		break
	print(x)
