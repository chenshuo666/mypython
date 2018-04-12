week={}
week['Monday']='星期五'
week['Saturdy']='星期一'
week['Tuesday']='星期二'
week['Wednesday']='星期三'
week['Thursday']='星期四'
week['Friday']='星期五'
week['Saturday']='星期六'
week['Sunday']='星期日'

print(week)

# s=input("请入你要查询的单词：")
# q=week[s]
# print(q)

dict_keys=week.keys()
print(dict_keys) #获取词典的键值
dict_values=week.values()
print(dict_values)#获取词典的value

dl=week.copy()#拷贝词典
print(dl)

r=week.get("Friday")#查询指定键值的value
print(r)

s=week.items()#将词典转化成tuple样式
print(s)

# w=week.get("星期三")//get()方法只能获取键值
# print(w)

g=week.keys()#获取词典的所有键值
print(g)

o=week.values()#获取词典的所有value值
print(o)

y=type(week)
print(y)

a={}
a={1,2,3,4,5,6}#set集合
nj=type(a)
print(nj)

b={2,4,6,8,0}
sd=a& b#set集合的与运算
print(sd)
sf=a^ b#set集合的异或运算
print(sf)

yu=[2,4,1,5,8,4,7,5,9,12]
aw=sorted(yu)
print(aw)

po=pow(9,6)#X的Y次方
print(po)

rt=max(yu)
print(rt)



