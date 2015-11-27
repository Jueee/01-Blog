'''
上下文管理器(context manager)
它是Python2.5开始支持的一种语法，用于规定某个对象的使用范围。
一旦进入或者离开该使用范围，会有特殊操作被调用 (比如为对象分配或者释放内存)。

它的语法形式是 with...as...
'''

'''
关闭文件
上下文管理器可以在不需要文件的时候，自动关闭文件。

上下文管理器有隶属于它的程序块。
当隶属的程序块执行结束的时候 (也就是不再缩进)，上下文管理器自动关闭了文件 (我们通过f.closed来查询文件是否关闭)。
我们相当于使用缩进规定了文件对象f的使用范围。
'''
# 程序一
f = open('test.txt','a')
print(f.closed)
f.write("Hello World!")
f.close()
print(f.closed)

# 程序二
with open("test.txt",'a') as f:
	print(f.closed)
	f.write("Hello World! \n")
print(f.closed)
print(f)
dir()



'''
自定义

任何定义了 __enter__() 和 __exit__()方法的对象都可以用于上下文管理器。
文件对象f是内置对象，所以f自动带有这两个特殊方法，不需要自定义。
'''
class VOW(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = "I say: " + self.text    # add prefix
        return self                          # note: return an object
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text + "!"          # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)




