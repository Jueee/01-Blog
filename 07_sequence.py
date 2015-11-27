'''
序列(sequence)
序列包含有定值表(tuple)和表(list)。

此外，字符串(string)是一种特殊的定值表。
表的元素可以更改，定值表一旦建立，其元素不可更改。

任何的序列都可以引用其中的元素(item)。
'''


n = [1,2,4,4,3,5,2,'we',34]
print(n.count(9))	#计数
print(n.index(4))	#查询第一次出现的下标
n.append(True)		#增加元素
print(n)

a=[1,3,2,36,457,5]
a.sort()		#排序
print(a)

print(n.pop())# 从n中去除最后一个元素，并将该元素返回。
print(n)

n.remove(2)	# 从nl中去除第一个2
print(n)

n.insert(3,'asd')	#在下标为3的位置插入字符
print(n)

print([1,2,3] + [4,5,6])

#会有错误信息，说明该运算符“-”没有定义。
#print([1,2,3] - [3,4])

#现在我们继承list类，添加对"-"的定义
class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]        
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print(superList([1,2,3,5]) - superList([3,4]))

print(len(a))	#内置函数len()用来返回list所包含的元素的总数。



print('-----------------------')
s = [0,1,2,3,4,5,3]
print(len(s))         #返回： 序列中包含元素的个数
print(min(s))         #返回： 序列中最小的元素
print(max(s))         #返回： 序列中最大的元素
print(all(s))         #返回： True, 如果所有元素都为True的话
print(any(s))         #返回： True, 如果任一元素为True的话
s1 = [1]			  # 1 True 0 False
print(any(s1))


print(sum(s))         #返回：序列中所有元素的和

# x为元素值，i为下标(元素在序列中的位置)

print(s.count(3))     #返回： x在s中出现的次数

print(s.index(4))     #返回： x在s中第一次出现的下标

print(type(s))


#由于定值表的元素不可变更，下面方法只适用于表:
print('-----------------------')
l = [0,1,2,3,4,5,3]
l2 = [0,1,2,3,4,5,3]
# l为一个表, l2为另一个表

l.extend(l2)       #在表l的末尾添加表l2的所有元素
print(l)
l.append(4) 			  #在l的末尾附加x元素
print(l)       
l.sort()           #对l中的元素排序
print(l)
l.reverse()       #将l中的元素逆序
print(l)
a = l.pop()            #返回：表l的最后一个元素，并在表l中删除该元素
print(l,'---',a)
del l[4]			      #删除该元素
print(l)