'''
Python 还是一个多范式语言 (multi-paradigm)

Python 的多范式依赖于 Python 对象中的特殊方法 (special method)。特殊方法名的前后各有两个下划线。
特殊方法又被成为魔法方法(magic method)，定义了许多Python语法和表达方式.
当对象中定义了特殊方法的时候，Python也会对它们有“特殊优待”。
比如定义了__init__()方法的类，会在创建对象的时候自动执行__init__()方法中的操作。

可以通过dir()来查看对象所拥有的特殊方法，比如dir(1)
'''

'''
运算符
Python的运算符是通过调用对象的特殊方法实现的。
在Python中，运算符起到简化书写的功能，但它依靠特殊方法实现。
'''
print('abc' + 'xyz')

print((1.8).__mul__(2.9))
print(True.__or__(False))


'''
内置函数
Python的内置函数是通过调用对象的特殊方法实现的。
'''
print(len([1,2,3,4,5]))
print([1,2,3,4].__len__())

print((-1).__abs__())
print((2.8).__int__())


'''
表(list)元素引用
'''
li = [1,2,3,4]
print(li[3])
#上面的程序运行到li[3]的时候，Python发现并理解[]符号，然后调用__getitem__()方法。
print(li.__getitem__(2))
li.__setitem__(3,0)
print(li)

t = {'a':1, 'b':4}
t.__delitem__('a')
print(t)


'''
函数
在Python中，函数也是一种对象。
实际上，任何一个有__call__()特殊方法的对象都被当作是函数。
'''
class SampleMore(object):
	"""docstring for SampleMore"""
	def __call__(self, arg):
		return arg**5
add = SampleMore()
print(add(3))

# add 还可以作为函数对象，被传递给map()函数。
m = map(add,[2,4,5,6,9])
print(list(m))

		