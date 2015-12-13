'''
删除


'''

import sqlite3

conn = sqlite3.connect('SQLite.db')

c = conn.cursor()

c.execute('UPDATE book set price=? where id=?', (1000,1))
c.execute('DELETE from book where id=2')
c.execute('DELETE from category')


# 也可以直接删除整张表：
c.execute('DROP TABLE book')
c.execute('DROP TABLE category')

# 如果删除test.db，那么整个数据库会被删除。

conn.commit()
conn.close()
