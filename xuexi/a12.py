import sqlite3
conn=sqlite3.connect('scores.sqlite')
cursor=conn.execute('select * from student;')
for row in cursor:
    print('No {}:{}'.format(row[0],row[1]))

s=cursor.fetchone#取得当前的一行数据
print(s)

cursor.fetchall()#取得剩余的数据