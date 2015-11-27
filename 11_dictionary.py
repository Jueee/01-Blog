'''
词典 (dictionary)
与列表相似，词典也可以储存多个元素。这种储存多个元素的对象称为容器(container)。
词典的元素包含有两部分，键和值，常见的是以字符串来表示键，值可以是任意对象。键和值两者一一对应。
词典的元素没有顺序，不能通过下标引用元素。词典是通过键来引用的。

'''
dic = {'tom':11,'sam':45,'lily':102}
print(dic,type(dic))
print(dic['tom'])	#通过键来引用。
dic['tom'] = 33		#修改词典的值。
print(dic)

dic2= {}
print(dic2,type(dic2))
dic2['lilei'] = 22	#在词典中增添一个新元素
print(dic2)

#在循环中，dict的每个键，被提取出来，赋予给key变量。
for key in dic:
	print(key,'---',dic[key])

print(dic.keys())		# 返回dic所有的键
print(dic.values())		# 返回dic所有的值
print(dic.items())		# 返回dic所有的元素（键值对）
#print(dic.clear())		# 清空dic，dict变为{}

del(dic['tom'])			# 删除 dic 的‘tom’元素
print(dic)

print(len(dic))			# 用len()查询词典中的元素总数。