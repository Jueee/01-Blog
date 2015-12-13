'''
sqlite3

Python自带一个轻量级的关系型数据库 SQLite 。这一数据库使用SQL语言。
'''



'''
下面创建一个简单的关系型数据库，为一个书店存储书的分类和价格。
数据库中包含两个表：category用于记录分类，book用于记录某个书的信息。
一本书归属于某一个分类，因此book有一个外键(foreign key)，指向catogory表的主键id。
'''


'''
创建数据库

在使用connect()连接数据库后，我就可以通过定位指针cursor，来执行SQL命令：
'''
import sqlite3

# SQLite的数据库是一个磁盘上的文件，如 SQLite.db，因此整个数据库可以方便的移动或复制。
# SQLite.db 一开始不存在，所以SQLite将自动创建一个新文件。
conn = sqlite3.connect('SQLite.db')

c = conn.cursor()

# create tables
c.execute('''CREATE table category 
				(id int primary key,
				 sort int, 
				 name text)''')
c.execute('''CREATE table book
				(id int primary key,
				 sort int,
				 name text,
				 price real,
				 category int,
				 foreign key(category) references category(id))''')

# save the changes
conn.commit()

# close the connection with the database
conn.close()

