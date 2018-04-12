#获取1到6的自然数
import random
a=random.randint(1,6)
print(a)
x=1;
while a!=6:
    x+=1
    a=random.randint(1,6)
    print(a)
print(" "+str(x))

#“:>2”表示靠右对齐，
for i in range(2,7,4):
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}*{}={:>2}   ".format(k,j,k*j),end="")
        print()
    print()

#continue的作用，不满足条件时，执行上一个循环条件
for i in range(2,9):
    if i !=2 and i !=6 : continue #如果i既不是2也不是6的话就放弃接下来的语句而进入下一个i循环
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}*{}={:>2}   ".format(k, j, k * j), end="")
        print()
    print()

#enumerate()的作用，提取当前的索引和数值
names=['we','rt','er5','rwe','rew','uy']
for i,name in enumerate(names):#enumerate获取数列的索引和值
    print("NO.{}:{}\n".format(i,name))

#map的功能，map(执行用的函数，容器变量)
def pick(x):#定义自己书写的函数
    fruits=["Apple","Banana","Orange","Cherry","Pine Apple","Berry"]
    return fruits[x]
alist=[1,4,2,5,0,3,4,4,2]
choices=map(pick,alist)
for choice in choices:
    print(choice)


#迭代函数filter将每一个元素逐一拿出来交给第一个参数中所置顶的函数计算
import sympy
a,b=500,600
numbers=range(a,b)
prime_nums=filter(sympy.isprime##验证数字是否为质数
                  ,numbers)
print("prime numbers({}-{}):".format(a,b))
for prime_num in prime_nums:
    print(prime_num,end="*")
print("\n\n\n")

##凡是在try之内的语句只要出现任何异常，程序控制流程就会自动跑到except之下的语句
while True:
    try:
        age=int(input("What is your age?\n"))
        break
    except:
        print("Please input a number!")
if age<15:
    print("you are too young")
else:
    print("you are a men")




