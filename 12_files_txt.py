'''
文本文件读写
文本文件的读写主要通过open()所构建的文件对象来实现。
'''

# 创建文件对象
# 打开一个文件，并使用一个对象来表示该文件：f = open(文件名，模式)
# 最常用的模式有：(1)"r" 只读 (2)"w" 写入 (3)"a" 追加写入
f = open('E:/360/Python/Files/file.txt','r')

# 读取一行
line = f.readline()
print(line)

# 读取所有行，储存在列表中，每个元素是一行。
lines = f.readlines()
print(lines)

# 读取N bytes的数据
by = f.read(4)
print(by)

# 关闭文件
f.close()


w = open('E:/360/Python/Files/file.txt','w')
r = open('E:/360/Python/Files/file.txt','r')

# 将'I like apple'写入文件
w.write('I like apple')      
lines = r.readlines()
print(lines)

# 关闭文件
w.close()
r.close()


print(f.__dict__)