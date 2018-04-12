import sqlite3
def disp_menu():
    print("学生数据编辑")
    print("___________")
    print("1.新增")
    print("2.编辑")
    print("3.删除")
    print("4.显示所有的学生")
    print("0.结束")
    print("___________")
def append_data():
    while True:
        no=int (input("请输入学生座号（-1停止输入）："))
        if no ==-1:
            break
        name=input("请输入学生姓名：")
        conn=sqlite3.connect('scores.sqlite')
        sqlstr="select * from student where stdno={};".format(no)
        cursor=conn.execute(sqlstr)
        if len(cursor.fetchall())>0:
            print("你数输入的座号已经有人了！！")
        else:
            conn.execute("insert into student values({},{});".format(no,str(name)))
            conn.commit()

def edit_data():
    no=input("你输入要编辑的学生座号")
    conn=sqlite3.connect('scores.sqlite')
    cursor=conn.execute("select * from student where stdno={};".format(no))
    rows=cursor.fetchall()
    if len(cursor.fetchall()) > 0:
        print("当前的学生姓名：",rows[0][1])
        name= input("请输入学生姓名：")
        conn.execute("update student set name='{}' where stdno={};".format(name,no))
        conn.commit()
    else:
        print("找不到要编辑的学生座号")

def del_data():
    no=input("请输入你要删除的学生的座号：")
    conn = sqlite3.connect('scores.sqlite')
    cursor=conn.execute("select * from student where stdno={};".format(no))
    rows = cursor.fetchall()
    if len(rows)>0:
        print("你当前要删除的书座号{}的{}".format(rows[0][0],rows[0][1]))
        answer=input("你确定要删除吗？（Y/）")
        if answer=='Y' or answer=='y':
            conn.execute("delete from student where stdno={};".format(no))
            conn.commit()
            print("已删除制定的学生。。。")
        else:
            print("找不到要删除的学生")

def disp_data():
    conn = sqlite3.connect('scores.sqlite')
    cursor=conn.execute("select * from student;")
    for row in cursor:
        print ("NO{}:{}".format(row[0],row[1]))


while True:
    disp_menu()
    choice=int(input("请输入你的选择："))
    if choice==0:
        break
    elif choice==1:
        append_data()
    elif choice==2:
        edit_data()
    elif choice==3:
        del_data()
    elif choice==4:
        disp_data()
    else:break
