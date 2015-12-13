'''
正则表达式(regular expression)主要功能是从字符串(string)中通过特定的模式(pattern)，搜索想要找到的内容。


在Python中使用正则表达式需要标准库中的一个包re。
'''
import re

#re.search()接收两个参数，第一个就是我们所说的正则表达式
#re.search()搜索整个字符串，直到发现符合的子字符串。
m = re.search('[0-9]','asasd2d44s34af')
print(m,type(m),m.group())

#re.match()从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
n = re.match('[0-9]','3214323')   
print(n,type(n),n.group())


#str = re.sub(pattern, replacement, string) 
# 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
s = re.sub('[0-9]', 'WWW', 's23tr344ing')
print(s) 


# re.split()    
# 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
s = re.split('[0-9]','s2433twewe5sdfstwr344ing')
print(s)

# re.findall()  
# 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回
s = re.findall('[0-9]','s2433twewe5sdfstwr344ing')
print(s)




'''
返回控制

我们有可能对搜索的结果进行进一步精简信息。比如下面一个正则表达式：

output_(\d{4})

该正则表达式用括号()包围了一个小的正则表达式，\d{4}。 
这个小的正则表达式被用于从结果中筛选想要的信息（在这里是四位数字）。
这样被括号圈起来的正则表达式的一部分，称为群(group)。
我们可以m.group(number)的方法来查询群。
group(0)是整个正则表达的搜索结果，group(1)是第一个群……
'''
m = re.search("output_(\d{4})", "output_1986.txt")
print(m.group(1))

# 还可以将群命名，以便更好地使用m.group查询:
m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m.group("year"))



'''
正则表达式的常用语法：


1）单个字符:
.          任意的一个字符
a|b        字符a或字符b
[afg]      a或者f或者g的一个字符        
[0-4]      0-4范围内的一个字符
[a-f]      a-f范围内的一个字符
[^m]       不是m的一个字符
\s         一个空格
\S         一个非空格
\d         [0-9]
\D         [^0-9]
\w         [0-9a-zA-Z]
\W         [^0-9a-zA-Z]

2）重复
紧跟在单个字符之后，表示多个这样类似的字符
*         重复 >=0 次
+         重复 >=1 次
?         重复 0或者1 次
{m}       重复m次。比如说 a{4}相当于aaaa，再比如说[1-3]{2}相当于[1-3][1-3]
{m, n}    重复m到n次。比如说a{2, 5}表示a重复2到5次。小于m次的重复，或者大于n次的重复都不符合条件。

3) 位置
^         字符串的起始位置
$         字符串的结尾位置
'''






















