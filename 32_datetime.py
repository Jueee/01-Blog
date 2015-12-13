'''
datetime包

datetime包是基于time包的一个高级包， 为我们提供了多一层的便利。

datetime可以理解为date和time两个组成部分。
	date是指年月日构成的日期(相当于日历)
	time是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)

你可以将这两个分开管理(datetime.date类，datetime.time类)，也可以将两者合在一起(datetime.datetime类)。
'''

import datetime
t = datetime.datetime(2012,9,3,21,30,30)
print(t)

# 所返回的t有如下属性:
#	hour, minute, second, microsecond
#	year, month, day, weekday   # weekday表示周几
print("%2d:%2d:%2d" % (t.hour,t.minute,t.second))


'''
datetime包还定义了时间间隔对象(timedelta)。
一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。
比如今天的上午3点加上5个小时得到今天的上午8点。
'''
t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)

# 两个datetime对象还可以进行比较。
print(t > t_next)

'''
datetime对象与字符串转换

假如我们有一个的字符串，我们如何将它转换成为datetime对象呢？

一个方法是用上一讲的正则表达式来搜索字符串。
但时间信息实际上有很明显的特征，我们可以用格式化读取的方式读取时间信息。

我们通过format来告知Python我们的str字符串中包含的日期的格式。
在format中，%Y表示年所出现的位置, %m表示月份所出现的位置……。
'''
from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt" 
str    = "output-1997-12-23-030000.txt" 
t      = datetime.strptime(str, format)
print(t)


'''
我们也可以调用datetime对象的strftime()方法，来将datetime对象转换为特定格式的字符串。
'''
import datetime
tx = datetime.datetime(2012,9,5,23,30,29)
format = "output-%Y-%m-%d-%H%M%S.txt" 
print(tx.strftime(format))
