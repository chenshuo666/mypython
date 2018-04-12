##list用[]括号，
##tuple和list一样，用()盛放数据，数据不可修改
##set集合用{}，和dic的区别是{}中只有value
##dic集合用{}，由key和value组成，

s = "line1\nline2"#\n为换行字符
print(s)

pre="the sum is:"
sum=1+2+3+4+5
print(pre+str(sum))

a=38.0
b=type(s)#检测类型
print(b)

c=s.split()#取出str中的完整的词并放入到list中
print(c)

d=list(s)#将将str中的字符串拆成一个个的字符组成的列表
print(d)

x=list(range(10))#生成0到9的数字并放入到list中
print(x)
y=x[1:7]#前开后闭取出list(x)中的第一到第六的字符
print(y)
z=x[1:7:2]#隔两个索引取出字符
print(z)
del x[1:7:2]
print(x)

p=len(x)#计算列表的长度
print(p)

q=x.index(4)#返回列表第一次出现的n的索引值
print(q)
x.append(3)#将n插入到数列x的末尾
print(x)

x.sort()#将数列x进行排序
print("排序为："+str(x))


s=[2,3,4,2,4,8,1,78]
m=list(s)
print("m="+str(m))
x.extend(m)#将数列m全部添加到数列x之后
print(x)

x.insert(2,m)#将数列插入到指定的位置
print(x)

f=x.pop()#弹出数列的最后一个索引指向的元素
print(f)

g=x.remove(2)#从列表中删除第一个出现的元素n
print(x)

x.reverse()#反转列表的顺序
print(x)



