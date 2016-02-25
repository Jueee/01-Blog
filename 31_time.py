'''
时间和日期管理功能

'''
import time				
print(time.time())
print(time.clock())


# time.sleep()可以将程序置于休眠状态，直到某时间间隔之后再唤醒程序，让程序继续运行。
print('start')
time.sleep(1)		# sleep for 1 seconds
print('wake up')


# struct_time对象
# 该对象实际上是将挂钟时间转换为年、月、日、时、分、秒……等日期信息，存储在该对象的各个属性中(tm_year, tm_mon, tm_mday...)。

st = time.gmtime()		# 返回struct_time格式的UTC时间
print(st)

st = time.localtime()	# 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print(st)
print(st.tm_year,st.tm_min,type(st.tm_min))
print(str(st.tm_year) + '-' + str(st.tm_mon) + '-' + str(st.tm_mday),str(st.tm_hour) + ':' + str(st.tm_min) + ':' + str(st.tm_sec))

s = time.mktime(st)		# 将struct_time格式转换成wall clock 
print(s)

ISOTIMEFORMAT='%Y-%m-%d %X'
s = time.strftime( ISOTIMEFORMAT,time.localtime())
print(s)
















