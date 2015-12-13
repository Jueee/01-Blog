'''
os.path包主要是处理路径字符串

比如说'/home/vamei/doc/file.txt'，提取出有用信息。
'''
import os.path

#在python脚本里面使用那些不再PYTHONPATH上的第三方包或是自己编写的模块
import sys
sys.path.append('../88Apply')
import A05_timeFormat as timeFormat

path = 'E:\\360\\Python\\PythonCode\\01Study\\33_package-os.path.py'

print(os.path.basename(path))			# 查询路径中包含的文件名
print(os.path.dirname(path))			# 查询路径中包含的目录

info = os.path.split(path)				# 将路径分割成文件名和目录两个部分，放在一个表中返回
print(info)
print(info[0],info[1])


# 使用目录名和文件名构成一个路径字符串
path2 = os.path.join('E:\\', '360', 'Python', 'PythonCode', '88Apply', '03_Ascii.py')  
print(path2)


# 查询多个路径的共同部分
p_list = [path, path2]
print(os.path.commonprefix(p_list))

# 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'
print(os.path.normpath(path))


print(os.path.exists(path))			# 查询文件是否存在
print(os.path.getsize(path))		# 查询文件大小

print()
t = os.path.getatime(path)			# 查询文件上一次读取的时间
print(timeFormat.Time2ISOString(t))
t = os.path.getmtime(path)			# 查询文件上一次修改的时间
print(timeFormat.Time2ISOString(t))

print(os.path.isfile(path))			# 路径是否指向常规文件
print(os.path.isdir(path))			# 路径是否指向目录文件



