gg=int(input("请输入一个数值："))
m=0
s=0
for i in range(1,gg+1):
    s=i
    l = 0
    for k in range(1,i+1):
        l=k*(10**(s-1))+l
        s=s-1
    print('{}*8+{}'.format(l,i),end='')
    m=l*8+i
    print("={}".format(m))

m1=0
for i1 in range(1,gg+1):
    s1=i1
    l1 = 0
    for k1 in range(1,i1+1):
        l1=k1*(10**(s1-1))+l1
        s1=s1-1
    print('{}*9+{}'.format(l1,i1+1),end='')
    m1=l1*9+i1+1
    print("={}".format(m1))


