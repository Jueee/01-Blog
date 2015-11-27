'''
首先，def，这个关键字通知python：我在定义一个函数。square_sum是函数名。

括号中的a, b是函数的参数，是对函数的输入。参数可以有多个，也可以完全没有（但括号要保留）。

我们已经在循环和选择中见过冒号和缩进来表示的隶属关系。

c = a**2 + b**2        # 这一句是函数内部进行的运算

return c               # 返回c的值，也就是输出的功能。Python的函数允许不返回值，也就是不用return。

return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。

return a,b,c          # 相当于 return (a,b,c)

在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。return并不是必须的，当没有return, 或者return后面没有返回值时，函数将自动返回None。
None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。None多用于关键字参数传递的默认值。
'''
def square_sum(a,b):
	c = a**2 + b**2
	return c,a,b

print(square_sum(2,3),square_sum(2,3)[0])

'''
对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）
但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）
'''
#我们将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化。
a = 1
def change_integer(a):
    a = a + 1
    return a

print(change_integer(a))
print(a)
#我们将一个表传递给函数，函数进行操作，原来的表b发生变化。
b = [1,2,3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print(change_list(b))
print(b)


#lambda函数
#lambda生成一个函数对象。该函数参数为x,y，返回值为x+y。函数对象赋给func。
func = lambda x,y:x**2+y**2
print(func(3,4))

#函数作为参数传递
#将func传递给f，test中的f()就拥有了func()的功能。
def test(f,a,b):
	print('test',f(a,b))
test(func,3,4)

test((lambda x,y:x**y),6,3)

#map()函数
#map()有两个参数，一个是lambda所定义的函数对象，一个是包含有多个元素的表。
#map()的功能是将函数对象依次作用于表的每一个元素，每次作用的结果储存于返回的表re中
re = map((lambda x:x+3),[1,2,4,5])
#在Python 3.X中，map()的返回值是一个循环对象。可以利用list()函数，将该循环对象转换成表。
print(list(re))
#map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。
re2 = map((lambda x,y:x+y),[1,2,3],[5,7,9])
print('re2:',list(re2))
print(re2)

#filter()函数
#filter通过读入的函数来筛选数据：如果函数对象返回的是True，则该次的元素被储存于返回的表中。
#在Python 3.X中，filter返回的不是表，而是循环对象。
print(list(filter((lambda x:x>100),[10,20,100,200,400])))


#reduce()函数
#reduce函数的第一个参数也是函数，但有一个要求，就是这个函数自身能接收两个参数。reduce可以累进地将函数作用于各个参数。
#在Python 3里，reduce()函数已经被从全局名字空间里移除了，它现在被放置在fucntools模块里
from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4,5,6,7,8,9]))