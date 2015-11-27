'''
参数(arguments)传递

在定义或者调用参数时，参数的几种传递方式可以混合。但在过程中要小心前后顺序。
基本原则是，先位置，再关键字，再包裹位置，再包裹关键字
'''
#位置传递
def f(a,b,c):
	return a**2+b+c

print(f(1,3,5))

#关键字传递
#关键字(keyword)传递是根据每个参数的名字传递参数。
print(f(c=1,b=2,a=3))

#关键字传递可以和位置传递混用。但位置参数要出现在关键字参数之前：
print(f(5,c=3,b=2))

#参数默认值
#给参数赋予默认值(default)。如果该参数最终没有被传递值，将使用该默认值。
def fun2(a,b,c=10):
	return a*b+c

print(fun2(3,5))
print(fun2(3,5,6))


#包裹传递
#在定义函数时，我们有时候并不知道调用的时候会传递多少个参数。
#这时候，包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会非常有用。

#包裹位置传递:作为包裹位置传递所用的元组名，在定义func时，前应加*号。
def fun3(*name):
	print(name,type(name))

fun3(1,2,3,'a',True)
fun3(True)
fun3(2,5)

#包裹关键字传递:参数dict是包裹关键字传递所用的字典，在dict前加**。
def fun4(**dict):
	print(dict,type(dict))
fun4(a=1,b=3)


#解包裹
#*和**，也可以在调用的时候使用，即解包裹(unpacking)
#所谓的解包裹，就是在传递tuple时，让tuple的每一个元素对应一个位置参数。
def fun5(a,b,c):
	print(a,b,c,a+b+c)
arg = (1,4,5)
fun5(*arg)
fun5(arg,arg,arg)
#对词典的解包裹:在传递词典dict时，让词典的每个键值对作为一个关键字传递给func。
dic = {'a':1,'b':2,'c':4}
fun5(**dic)