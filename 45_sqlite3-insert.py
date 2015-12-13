'''
插入数据

插入数据同样可以使用execute()来执行完整的SQL语句。

上面创建了数据库和表，确立了数据库的抽象结构。下面将在同一数据库中插入数据：
'''
import sqlite3

conn = sqlite3.connect('SQLite.db')

c = conn.cursor()

books = [(1, 2, 'Cook', 3.12, 1),
		 (2, 3, 'Python Intro', 17.5, 2),
		 (3, 2, 'OS Intro', 13.6, 2)]

# execute "INSERT" 
c.execute("INSERT into category values(1, 2, 'kitchen')")

# using the placeholder
# execute函数第2个参数接收的是元组, 而非列表。
# SQL语句中的参数，使用"?"作为替代符号，并在后面的参数中给出具体值。
# 这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击。
c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'computer'))

# execute multiple commands
# 也可以用executemany()的方法来执行多次插入，增加多个记录。每个记录是表中的一个元素
c.executemany("INSERT into book values(?, ?, ?, ?, ?)", books)

conn.commit()
conn.close()