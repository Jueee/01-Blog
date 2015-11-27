'''
内存管理 
'''

'''
对象的内存使用
Python是动态类型的语言(参考动态类型)，对象与引用分离。

为了探索对象在内存的存储，我们可以求助于Python的内置函数id()。它用于返回对象的身份(identity)。
其实，这里所谓的身份，就是该对象的内存地址。
'''
a = 1
print(id(a))			# 内存地址的十进制表示
print(hex(id(a)))		# 内存地址的十六进制表示

#当我们创建多个等于1的引用时，实际上是让所有这些引用指向同一个对象。
b = 1
print(id(a),id(b))

#为了检验两个引用指向同一个对象，我们可以用is关键字。
#is用于判断两个引用所指的对象是否相同。
# True
a = 1
b = 1
print(a is b)

# True
a = "good"
b = "good"
print(a is b)

# False
a = "very good morning"
b = "very good morning"
print(a is b)

# False
a = []
b = []
print(a is b)



'''
在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count)。

我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。

需要注意的是，当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。
因此，getrefcount()所得到的结果，会比期望的多1。
'''
from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = a
print(getrefcount(b))

'''
对象引用对象
'''
class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))


from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))


'''
容器对象的引用可能构成很复杂的拓扑结构。

我们可以用objgraph包来绘制其引用关系。
objgraph是Python的一个第三方包。安装之前需要安装xdot。
objgraph官网：	http://mg.pov.lt/objgraph/	
				https://pypi.python.org/pypi/objgraph
'''

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
objgraph.show_refs([z], filename='ref_topo.png')


#两个对象可能相互引用，从而构成所谓的引用环(reference cycle)。

a = []
b = [a]
a.append(b)

#即使是一个对象，只需要自己引用自己，也能构成引用环。

a = []
a.append(a)
print(getrefcount(a))



#某个对象的引用计数可能减少。比如，可以使用del关键字删除某个引用:

from sys import getrefcount

a = [1, 2, 3]
b = a
print(getrefcount(b))

del a
print(getrefcount(b))

#del也可以用于删除容器元素中的元素，比如:

a = [1,2,3]
del a[0]
print(a)


#如果某个引用指向对象A，当这个引用被重新定向到某个其他对象B时，对象A的引用计数减少:

from sys import getrefcount

a = [1, 2, 3]
b = a
print(getrefcount(b))

a = 1
print(getrefcount(b))