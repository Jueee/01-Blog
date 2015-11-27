#range()
#使用过range()来控制for循环
s='asfafsdfasdfad'
for i in range(0,len(s),2):
	print(s[i])




#enumerate()
#利用enumerate()函数，可以在每次循环中同时得到下标和元素
#实际上，enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)，两个元素分别赋予index和char
s ='qwqreqrwetery'
for (index,char) in enumerate(s):
	print(index,char)


#zip()
#如果你多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，可以利用zip()方便地实现
#每次循环时，从各个序列分别从左到右取出一个元素，合并成一个tuple，然后tuple的元素赋予给a,b,c
ta = [1,2,3]
tb = [92.23,34.23,43.5]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
	print(a,b,c)

zip1 = zip(ta,tb)
print(zip1)

na,nb = zip(*zip1)
print(na,nb)


#python3以后迭代器不在是.next(),而是__next__(),
f = open('E:/360/Python/Files/file.txt')
'''
当一个循环结构（比如for）调用循环对象时，它就会每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，停止调用next()。
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
'''
for line in f:
	print(line)

'''
迭代器

从技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。
'''

'''
生成器

生成器(generator)的主要目的是构成一个用户自定义的循环对象。

生成器的编写方法和函数定义类似，只是在return的地方改为yield。
生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。
当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。
生成器自身又构成一个循环器，每次循环使用一个yield返回的值。
'''
def gen():
	a = 100
	yield a
	a = a*8
	yield a
	yield 1000
for i in gen():
	print(i)


def gen2():
	for i in range(5):
		yield i
#生成器表达式(Generator Expression):生成器表达式是生成器的一种简便的编写方式。
G = (x for x in range(5))
for i in gen2():
	print(i)
for i in G:
	print(i)


#表推导
#表推导(list comprehension)是快速生成表的方法。

L = []
for x in range(5):
	L.append(x**2)
#表推导的方式:
print(L)

L2 = [x**2 for x in range(7)]
print(L2)

x1=[1,3,5]
y1=[9,12,13]
L3 = [x**2 for (x,y) in zip(x1,y1) if y>10]
print(L3)