



import random
'''
如果你已经了解伪随机数(psudo-random number)的原理，那么你可以使用如下:
random.seed(x)
来改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
'''



'''
1) 随机挑选和排序
random.choice(seq)   # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
random.sample(seq,k) # 从序列中随机挑选k个元素
random.shuffle(seq)  # 将序列的所有元素随机排序
'''
print(random.choice(range(10)))
print(random.sample(range(10),5))
a = ['1','2','3','4','5']
random.shuffle(a)
print(a)

a = list(range(15))
random.shuffle(a)
print(a)


'''
2）随机生成实数

下面生成的实数符合均匀分布(uniform distribution)，意味着某个范围内的每个数字出现的概率相等:
random.random()          # 随机生成下一个实数，它在[0,1)范围内。
random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内。

下面生成的实数符合其它的分布 (你可以参考一些统计方面的书籍来了解这些分布):
random.gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。 
random.expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。
'''
print(random.random())
print(random.uniform(10,20))



'''
假设我们有一群人参加舞蹈比赛，为了公平起见，我们要随机排列他们的出场顺序。
'''
all_people = ['Tom','Paul','Jane','Manu','Jue']
random.shuffle(all_people)
for i in range(len(all_people)):
	print(i,all_people[i])

for i,name in enumerate(all_people):
	print(i ,":" + name)