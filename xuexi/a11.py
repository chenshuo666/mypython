import sqlite3
conn=sqlite3.connect('scores.sqlite')#链接数据库
conn.execute('insert into student values(1,"王小明");')#执行数据哭操作
conn.commit()#把之前的改变确实反应到数据库中，数据库改变之后一定要调用该函数，以免程序结束之后没有顺利的将数据存到数据库中
#conn.rollback()#取消当前变更，恢复上一次commit时的状态
conn.close()#关闭数据库
