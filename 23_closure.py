'''
闭包(closure)

闭包(closure)是函数式编程的重要的语法结构。
函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)。

函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。
闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

闭包有效的减少了函数所需定义的参数数目。这对于并行运算来说有重要的意义。在并行运算的环境下，我们可以让每台电脑负责一个函数，然后将一台电脑的输出和下一台电脑
的输入串联起来。最终，我们像流水线一样工作，从串联的电脑集群一端输入数据，从另一端输出数据。这样的情境最适合只有一个参数输入的函数。闭包就可以实现这一目的。
'''



'''
函数对象的作用域
'''
def line_conf():
    def line(x):
        return 2*x+1
    print(line(5))   # within the scope


line_conf()
#print(line(5))       # out of the scope


'''
闭包
函数是一个对象，所以可以作为某个函数的返回结果。
'''
def line_conf():
    def line(x):
        return 2*x+1
    return line       # return a function object

#line_conf的返回结果被赋给line对象。上面的代码将打印11。
my_line = line_conf()
print(my_line(24))       



def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
#line所参照的b值是函数对象定义时可供参考的b值，而不是使用时的b值。
my_line = line_conf()
print(my_line(5))       


'''
一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。

在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
环境变量取值被保存在函数对象的__closure__属性中。
'''
def line_conf():
    b = 45
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)
print(my_line(23))




'''
在创建闭包的时候，我们通过line_conf的参数a,b说明了这两个环境变量的取值，这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。
我们只需要变换参数a,b，就可以获得不同的直线表达函数。
由此，我们可以看到，闭包也具有提高代码可复用性的作用。
'''
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))



def line_conf(a, b):
#   i = a * b           不能对外层变量赋值
    def line(x):
        i = a * b
        i = i + x
        return i * x + b
    return line
 
line1 = line_conf(4, 5)
print(line1(5))


def enclosing_function():
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n - 1)  # fails with NameError
    return factorial
factorial = enclosing_function()
for i in range(10):
    print(i,factorial(i))
print({factorial(n) for n in range(10) if n > 2})