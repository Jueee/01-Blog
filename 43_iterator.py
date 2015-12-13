'''
循环器(iterator)
'''

'''
在for i in iterator结构中，循环器每次返回的对象将赋予给i，直到循环结束。

使用iter()内置函数，我们可以将诸如表、字典等容器变为循环器。
'''

s = [2,4,6,8]
for i in iter(s):
	print(i)

'''
标准库中的itertools包提供了更加灵活的生成循环器的工具。这些工具的输入大都是已有的循环器。

另一方面，这些工具完全可以自行使用Python实现，该包只是提供了一种比较标准、高效的实现方式。
'''
import itertools


# 无穷循环器
itertools.count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...

itertools.cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...

itertools.repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...


# 函数式工具
'''
函数式编程是将函数本身作为处理对象的编程范式。在Python中，函数也是对象，因此可以轻松的进行一些函数式的处理，比如map(), filter(), reduce()函数。

itertools包含类似的工具。这些函数接收函数作为参数，并将结果返回为一个循环器。
'''
import itertools

# 包含元素1, 4, 27，即1**1, 2**2, 3**3的结果。函数pow(内置的乘方函数)作为第一个参数。
# pow()依次作用于后面两个列表的每个元素，并收集函数结果，组成返回的循环器。
rlt = map(pow, [1, 2, 3], [1, 2, 3])
for num in rlt:
    print(num)

# pow将依次作用于表的每个 tuple。
t = itertools.starmap(pow, [(1, 1), (2, 2), (3, 3)])
for num in t:
    print(num)

# 将lambda函数依次作用于每个元素，如果函数返回True，则收集原来的元素。6, 7
s = filter(lambda x: x > 5, [2, 3, 5, 6, 7])
for num in s:
    print(num)

# 与上面类似，但收集返回False的元素。2, 3, 5
s = itertools.filterfalse(lambda x: x > 5, [2, 3, 5, 6, 7])
for num in s:
    print(num)

# 当函数返回True时，收集元素到循环器。一旦函数返回False，则停止。1, 3
s = itertools.takewhile(lambda x: x < 5, [1, 3, 6, 7, 1])
for num in s:
    print(num)


# 当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器。6, 7, 1
s = itertools.dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1])
for num in s:
    print(num)




print('----------')

'''
组合工具

我们可以通过组合原有循环器，来获得新的循环器。
'''
# 连接两个循环器成为一个。1, 2, 3, 4, 5, 7
s = itertools.chain([1, 2, 3], [4, 5, 7])      
for num in s:
    print(num)

# 多个循环器集合的笛卡尔积。相当于嵌套循环 
s = itertools.product('abc', [1, 2])   
for num in s:
    print(num)

# 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
s = itertools.permutations('abc', 2)
for num in s:
    print(num)

print('----------')
# 与上面类似，但允许两次选出的元素重复。即多了aa, bb, cc
s = itertools.combinations_with_replacement('abc', 2) 
for num in s:
    print(num)



'''
groupby()

将key函数作用于原循环器的各个元素。

根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。
每个新的循环器以函数返回结果为标签。
'''
'''
这就好像一群人的身高作为循环器。我们可以使用这样一个key函数: 
1) 如果身高大于180，返回"tall"；
2) 如果身高底于160，返回"short";
3) 中间的返回"middle"。
最终，所有身高将分为三个循环器，即"tall", "short", "middle"。
'''
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
# groupby的功能类似于UNIX中的uniq命令。
# 分组之前需要使用sorted()对原循环器的元素，根据key函数进行排序，让同组元素先在位置上靠拢。
friends = sorted(friends, key = height_class)
for m, n in itertools.groupby(friends, key = height_class):
    print(m)
    print(list(n))



# 根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
s = itertools.compress('ABCD', [1, 1, 1, 0])  
for num in s:
    print(num)

# 类似于slice()函数，只是返回的是一个循环器
ls = ['a','b','c','d','e','f'] 
s = itertools.islice(ls, 3, 5)                        
for num in s:
    print(num)

# 类似于zip()函数，只是返回的是一个循环器。
listone = ['a','b','c']  
listtwo = ['11','22','abc']  
s = zip(listone, listtwo)                          
for num in s:
    print(num)



listone = ['a','b','c']  
for item in itertools.repeat(listone,3):  
    print(item)  
