'''
glob包最常用的方法只有一个, glob.glob()。

该方法的功能与Linux中的ls相似(参看Linux文件管理命令)，接受一个Linux式的文件名格式表达式(filename pattern expression)，列出所有符合该表达式的文件（与正则表达式类似），将所有文件名放在一个表中返回。


该文件名表达式的语法与Python自身的正则表达式不同 (你可以同时看一下fnmatch包，它的功能是检测一个文件名是否符合Linux的文件名格式表达式)。 如下：

Filename Pattern Expression      Python Regular Expression

*                                .*

?                                .

[0-9]                            same

[a-e]                            same

[^mnp]                           same

'''
# 用该命令找出 E:\\360\\Python\\PythonCode\\ 下的所有文件:
import glob
s = 'E:\\360\\Python\\PythonCode\\*'
l = glob.glob(s)
for t in range(len(l)):
	print(l[t])