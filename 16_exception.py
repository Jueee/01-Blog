'''
Python 异常处理

异常处理帮助人们debug，通过更加丰富的信息，让人们更容易找到bug的所在。异常处理还可以提高程序的容错性。

		异常				描述
		NameError			尝试访问一个没有申明的变量
		ZeroDivisionError	除数为0
		SyntaxError			语法错误
		IndexError			索引超出序列范围
		KeyError			请求一个不存在的字典关键字
		IOError				输入输出错误（比如你要读的文件不存在）
		AttributeError		尝试访问未知的对象属性
		ValueError			传给函数的参数类型不正确，比如给int()函数传入字符串形
'''

#如果我们在写程序的时候，知道这里可能犯错以及可能的犯错类型，我们可以针对该异常类型定义好”应急预案“。
re = iter(range(5))
try:
	for i in range(10):
	    print(re.__next__())
except StopIteration:	#如果except后面没有任何参数，那么表示所有的exception都交给这段程序处理。
	print('here is end',i)
print('Hello World')


try:
	print(a*2)
except TypeError:
	print("TypeError:")
except:
	print('Not Type Error & Error noted')

'''
如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。

如果try中没有异常，那么except部分将跳过，执行else中的语句。
finally是无论是否有异常，最后都要做的一些事情。

流程如下:
try->异常->except->finally
try->无异常->else->finally
'''
def test_fun():
	try:
		m = 1/0
	except NameError:
		print("Catch NameError in the sub-function")
try:
	test_fun()
except ZeroDivisionError:
	print('Catch error in the main program')



#抛出异常
print('lalala')
reise StopIteration
print('Hahaha')