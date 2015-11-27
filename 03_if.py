i = 0
x = 1
y = 1
z = 1
if i > 0:
	x = x+1
	y = y+5
else:
	z = z+4
print(x,y,z)

#这里有三个块，分别属于if, elif, else引领
i = 1

if i > 0:
    print('positive i')
    i = i + 1
elif i == 0:
    print('i is 0')
    i = i * 10
else:
    print('negative i')
    i = i - 1

print('new i:',i)


#if嵌套
i = 5
if i > 1:
	print('wee')
	if i > 2:
		print('wefefw')


'''
if语句之后的冒号

以四个空格的缩进来表示隶属关系, Python中不能随意缩进

if  <条件1>:

    statement

elif <条件2>:

    statement

elif <条件3>：

    statement

else:

    statement
'''