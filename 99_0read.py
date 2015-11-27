'''
file_object = open('E:\\aa\\test.txt')
try:
     all_the_text = file_object.read()
     print(all_the_text)
finally:
     file_object.close()
'''
import re

file = open('E:/360/Python/Files/reportURL.txt')
a = ""
while 1:
    line = file.readline()
    if not line:
        break
    pass
    pattern1 = re.compile(r'(?:^|/?|&)raq=([^&]*)') 
    pattern2 = re.compile(r'raq.*/|raq.*=')
    match = pattern1.search(line) 
    if match: 
    # 使用Match获得分组信息
        mat = pattern2.sub(r'', match.group())
        a = a + mat + '\n' 
with open('E:/360/Python/Files/test.txt', 'a') as file:  
    file.write(a)  
    print(a)
file.close()  