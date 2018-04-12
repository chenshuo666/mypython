#获取1到6的自然数
import random
a=random.randint(1,6)
print(a)
x=1
q=0
w=0
e=0
r=0
t=0
y=0

while a!=6:
    x+=1
    if a == 1:
        q += 1
    elif a == 2:
        w += 1
    elif a == 3:
        e += 1
    elif a == 4:
        r += 1
    elif a == 5:
        t += 1
    a=random.randint(1,6)
    print(a)


y=x-(q+w+e+r+t)
print("总次数为："+str(x))
print("出现1的次数为：{}  &&1所占的百分比为：{}".format(str(q),str(q/x)))
print("出现2的次数为：{}  &&2所占的百分比为：{}".format(str(w),str(w/x)))
print("出现3的次数为：{}  &&3所占的百分比为：{}".format(str(e),str(e/x)))
print("出现4的次数为：{}  &&4所占的百分比为：{}".format(str(r),str(r/x)))
print("出现5的次数为：{}  &&5所占的百分比为：{}".format(str(t),str(t/x)))
print("出现6的次数为：{}  &&6所占的百分比为：{}".format(str(y),str(y/x)))