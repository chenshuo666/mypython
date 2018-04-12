def add(a,b):
    global d
    global c
    c=a+b
    d=a+b
    print("在函数中，(c={},d={})".format(c,d))
    return c

c=10
d=99
print("调用函数前，(c={},d={})".format(c,d))
print("{}+{}={}".format(2,2,add(2,2)))#{}和format是一一对应的关系
print("调用函数后，(c={},d={})".format(c,d))