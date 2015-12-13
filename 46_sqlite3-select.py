'''
查询

在执行查询语句后，Python将返回一个循环器，包含有查询获得的多个记录。

循环读取，也可以使用sqlite3提供的 fetchone() 和 fetchall() 方法读取记录：
'''

import sqlite3

conn = sqlite3.connect('SQLite.db')

c = conn.cursor()


# retrieve one record
c.execute('SELECT * from category order by sort')
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())

# retrieve all records as a list
c.execute('SELECT * from book where book.category=1')
print(c.fetchall())
print('--------')

# 更新数据库
c.execute('UPDATE book SET price=? WHERE id=?',(10, 1))

# iterate through the records
t = c.execute('SELECT name, price from book order by sort')
for row in t:
	print(row)