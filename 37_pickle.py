'''
存储对象 (pickle包，cPickle包)
'''


'''
1) 将内存中的对象转换成为文本流：
'''
import pickle

class Bird(object):
	"""docstring for Bird"""
	hava_feather = True
	way_of_reproduction = 'egg'

summer = Bird()
# 使用pickle.dumps()方法可以将对象summer转换成了字符串 
picklestring = pickle.dumps(summer)
print(picklestring)


'''
pickle生成的是二进制编码，所以在写文件和读文件时都需要附加‘b’标志：
写文件：
testFile = open('pickle.txt', 'wb')
读文件：
testFile = open('pickle.txt', 'rb')
否则open函数默认以文本方式打开文件
'''

fn = 'a.pkl'
with open(fn, 'wb') as f:
    # 使用pickle.dumps()方法可以将对象summer转换成了字符串 
    picklestring = pickle.dump(summer, f)
f.close()


'''
重建对象

首先，我们要从文本中读出文本，存储到字符串 (文本文件的输入输出)。
然后使用pickle.loads(str)的方法，将字符串转换成为对象。

要记得，此时我们的程序中必须已经有了该对象的类定义。
'''

fn = 'a.pkl'
with open(fn, 'rb') as f:
	summer = pickle.load(f)
	print(summer,summer.hava_feather,summer.way_of_reproduction)




'''
cPickle包

cPickle包的功能和用法与pickle包几乎完全相同 (其存在差别的地方实际上很少用到)，不同在于cPickle是基于c语言编写的，速度是pickle包的1000倍。对于上面的例子，如果想使用cPickle包，我们都可以将import语句改为:

import cPickle as pickle
就不需要再做任何改动了。
'''


