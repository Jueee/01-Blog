'''
装饰器(decorator)是一种高级Python语法。

装饰器可以对一个函数、方法或者类进行加工。
'''

# get square sum
def square_sum(a, b):
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))


# modify: print input

# get square sum
def square_sum(a, b):
    print("intput:", a, b)
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    print("input", a, b)
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))


'''
装饰器可以用def的形式定义，如下面代码中的decorator。

装饰器接收一个可调用对象作为输入参数，并返回一个新的可调用对象。
装饰器新建了一个可调用对象，也就是上面的new_F。
new_F中，我们增加了打印的功能，并通过调用F(a, b)来实现原有函数的功能。

定义好装饰器后，我们就可以通过@语法使用了。
在函数square_sum和square_diff定义之前调用@decorator，我们实际上将square_sum或square_diff传递给decorator，并将decorator返回的新的可调用对象赋给原来的函数名(square_sum或square_diff)。
'''

def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))



#含参的装饰器

# a new wrapper layer
def pre_str(pre=''):
    # old decorator
    def decorator(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)
        return new_F
    return decorator

# get square sum
@pre_str('^_^')
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@pre_str('T_T')
def square_diff(a, b):
    return a**2 - b**2
#该调用相当于:square_sum = pre_str('^_^') (square_sum)
print(square_sum(3, 4))
print(square_diff(3, 4))


#装饰类
#一个装饰器可以接收一个类，并返回一个类，从而起到加工类的效果。

def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()