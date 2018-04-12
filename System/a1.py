a=[1,2,3]
b=a
b[:]=[x+1 for x in a]
print(a,b)
b = [x-1 for x in a]
print(a,b)
