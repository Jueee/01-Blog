'''
Python一切皆对象(object)，每个对象都可能有多个属性(attribute)。


对象的属性可能来自于其类定义，叫做类属性(class attribute)。类属性可能来自类定义自身，也可能根据类定义继承来的。
一个对象的属性还可能是该对象实例定义的，叫做对象属性(object attribute)。
'''
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)

#对象的属性储存在对象的__dict__属性中。
#__dict__为一个词典，键为属性名，对应的值为属性本身。

print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)

'''
Python中的属性是分层定义的，比如这里分为object/bird/chicken/summer这四层。
当我们需要调用某个属性的时候，Python会一层层向上遍历，直到找到那个属性。
'''
#下面两种属性修改方法等效：
summer.__dict__['age'] = 3
print(summer.__dict__['age'])

summer.age = 5
print(summer.age)


'''
特性(property)
特性是特殊的属性。
比如我们为chicken类增加一个特性adult。当对象的age超过1时，adult为True；否则为False：

'''
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def getAdult(self):
        if self.age > 1.0: return True
        else: return False
    adult = property(getAdult)   # property is built-in

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)
summer.age = 2.5
print(summer.adult)


'''
特性使用内置函数property()来创建。
property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。
'''
class num(object):
    def __init__(self, value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self, value):
        self.value = value**2
    def delNeg(self):
        print("value also deleted")
        del self.value
    neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg

'''
使用特殊方法 __getattr__

我们可以用 __getattr__(self, name)来查询即时生成的属性。
当我们查询一个属性时，如果通过__dict__方法无法找到该属性，那么Python会调用对象的__getattr__方法，来即时生成该属性。
'''
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0: return True
            else: return False
        else: print(name)

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)

summer.male
summer.adafsa








