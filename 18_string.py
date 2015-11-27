'''
下面是一些用于字符串的方法。

尽管字符串是定值表的特殊的一种，但字符串(string)类有一些方法是改变字符串的。

这些方法的本质不是对原有字符串进行操作，而是删除原有字符串，再建立一个新的字符串，所以并不与定值表的特点相矛盾。
'''
#str为一个字符串，sub为str的一个子字符串。s为一个序列，它的元素都是字符串。width为一个整数，用于说明新生成字符串的宽度。


str = "  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  "
sub = "s"

print(str.count(sub)			,'返回：sub在str中出现的次数                                                            ')
print(str.find(sub)				,'返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1           ')
print(str.index(sub)			,'返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误          ')
print(str.rfind(sub)			,'返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1           ')
print(str.rindex(sub)			,'返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误          ')
print(str.isalnum()				,'返回：True， 如果所有的字符都是字母或数字                                             ')
print(str.isalpha()				,'返回：True，如果所有的字符都是字母                                                    ')
print(str.isdigit()				,'返回：True，如果所有的字符都是数字                                                    ')
print(str.istitle()				,'返回：True，如果所有的词的首字母都是大写                                              ')
print(str.isspace()				,'返回：True，如果所有的字符都是空格                                                    ')
print(str.islower()				,'返回：True，如果所有的字符都是小写字母                                                ')
print(str.isupper()				,'返回：True，如果所有的字符都是大写字母                                                ')
print(str.join(str)				,'返回：将s中的元素，以str为分割符，合并成为一个字符串。                                ')
print(str.strip()				,'返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub .  ')	#当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
print(str.replace(sub,"new_sub")	,'返回：用一个新的字符串new_sub替换str中的sub                                           ')
print(str.capitalize()			,'返回：将str第一个字母大写                                                             ')
print(str.lower()				,'返回：将str全部字母改为小写                                                           ')
print(str.upper()				,'返回：将str全部字母改为大写                                                           ')
print(str.swapcase()			,'返回：将str大写字母改为小写，小写改为大写                                             ')
print(str.title()				,'返回：将str的每个词(以空格分隔)的首字母大写                                           ')
print(str.center(100)			,'返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。           ')
print(str.ljust(100)			,'返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。         ')
print(str.rjust(100)			,'返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。         ')
 

print(str.split(','))    		#返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
print(str.split(',',0)) 
print(str.split(',',1)) 
print(str.split(',',2)) 
print(str.split(',',-1)) 		#b.split("..",-1)等价于b.split("..") 
print(str.rsplit(','))   		#返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符

 
#join用来连接字符串
li = ['my','name','is','bob'] 
aa = str.join(li) 
print(aa)

aa = ' '.join(li) 
print(aa)







print('===========================================================================')
print('===========================================================================')
print('===========================================================================')
'''
数学运算
'''
print(abs(-5)         )               # 取绝对值，也就是5
print(round(2.6)      )               # 四舍五入取整，也就是3.0
print(pow(2, 3)       )               # 相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
#print(cmp(2.3, 3.2)   )              # 3.X  没有该函数 比较两个数的大小
print(divmod(9,2)     )               # 返回除法结果和余数
print(max([1,5,2,9])  )               # 求最大值
print(min([9,2,-4,2]) )               # 求最小值
print(sum([2,-1,9,12]))               # 求和
print('----------')
'''
类型转换
'''
print(int("5")      )                   # 转换为整数 integer
print(float(2)      )                   # 转换为浮点数 float
#print(long("23")    )                   # 转换为长整数 long integer
#print(str(2.3)      )                   # 转换为字符串 string
print(repr(2.3)      )                   # 转换为字符串 repr
print(complex(3, 9) )                   # 返回复数 3 + 9i
print(ord("A")      )                   # "A"字符对应的数值
print(chr(65)       )                   # 数值65对应的字符
#print(unichr(65)    )                   # 数值65对应的unicode字符
print(bool(0)       )                   # 转换为相应的真假值，在Python中，0相当于False
print('----------')
'''
在Python中，下列对象都相当于False： [], (), {}, 0, None, 0.0, ''
'''
print(bin(56)                       )   # 返回一个字符串，表示56的二进制数
print(hex(56)                       )   # 返回一个字符串，表示56的十六进制数
print(oct(56)                       )   # 返回一个字符串，表示56的八进制数
print(list((1,2,3))                 )   # 转换为表 list
print(tuple([2,3,4])                )   # 转换为定值表 tuple
print(slice(5,2,-1)                 )   # 构建下标对象 slice
print(dict(a=1,b="hello",c=[1,2,3]) )   # 构建词典 dictionary
print('----------')

'''
序列操作
'''
print(all([True, 1, "hello!"])     )    # 是否所有的元素都相当于True值
print(any(["", 0, False, [], None]))    # 是否有任意一个元素相当于True值
print(sorted([1,5,3])              )    # 返回正序的序列，也就是[1,3,5]
print(reversed([1,5,3])            )    # 返回反序的序列，也就是[3,5,1]
print(list(reversed([1,5,3])))
print('----------')


'''
类，对象，属性
'''
class Me(object):
    def test(self):
        print("Hello!")

def new_test():
    print("New Hello!")

me = Me()

print(hasattr(me, "test")          )     # 检查me对象是否有test属性
print(getattr(me, "test")          )     # 返回test属性
print(setattr(me, "test", new_test))     # 将test属性设置为new_test
print(delattr(me, "test")          )     # 删除test属性
print(isinstance(me, Me)           )     # me对象是否为Me类生成的对象 (一个instance)
print(issubclass(Me, object)       )     # Me类是否为object类的子类
print('----------')


'''
编译，执行
'''
print(repr(me) )                         # 返回对象的字符串表达
print(compile("print('Hello')",'test.py','exec')  )     # 编译字符串成为code对象
print(eval("1 + 1")     )                # 解释字符串表达式。参数也可以是compile()返回的code对象
exec("print('Hello')")            # 解释并执行字符串，print('Hello')。参数也可以是compile()返回的code对象
print('----------')
'''
其他
'''
#input("Please input:")            # 等待输入
globals()                         # 返回全局命名空间，比如全局变量名，全局函数名
locals()                          # 返回局部命名空间



'''
字符串格式化

Python中内置有对字符串进行格式化的操作%。

%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"


可以用如下的方式，对格式进行进一步的控制：

%[(name)][flags][width].[precision]typecode

(name)为命名

flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。

width表示显示宽度

precision表示小数点后精度
'''
'''
格式化字符串时，Python使用一个字符串作为模板。
模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。
Python用一个tuple将多个值传递给模板，每个值对应一个格式符。
'''
print("I'm %s. I'm %d years old!" %('尉勇强',23))
a = "I'm %s. I'm %d years old!" % ('尉勇强',23)
print(a)
#还可以用词典来传递真实值。
print("I'm %(name)s . I'm %(age)d year old!" % {'name':'tom','age':99})


print("%+10x" % 10)

#上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。
print("%.*f" % (12, 1.2))