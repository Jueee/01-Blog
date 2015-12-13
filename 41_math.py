'''

'''
import math
'''
math包主要处理数学相关的运算。math包定义了两个常数:
math.e   # 自然常数e
math.pi  # 圆周率pi
'''
print(math.e)
print(math.pi)

'''
此外，math包还有各种运算函数 (下面函数的功能可以参考数学手册)：
math.ceil(x)       # 对x向上取整，比如x=1.2，返回2
math.floor(x)      # 对x向下取整，比如x=1.2，返回1
math.pow(x,y)      # 指数运算，得到x的y次方
math.log(x)        # 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,base=10)
math.sqrt(x)       # 平方根
'''
print(math.ceil(1.4))
print(math.floor(1.99))
print(math.pow(2,9))
print(math.log(4))
print(math.sqrt(2))

''' 
三角函数: math.sin(x), math.cos(x), math.tan(x), math.asin(x), math.acos(x), math.atan(x)
这些函数都接收一个弧度(radian)为单位的x作为参数。

角度和弧度互换: math.degrees(x), math.radians(x)

双曲函数: math.sinh(x), math.cosh(x), math.tanh(x), math.asinh(x), math.acosh(x), math.atanh(x)

特殊函数： math.erf(x), math.gamma(x)
'''
