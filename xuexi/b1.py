l=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(i!=k)and(j!=k):
                l=l+1
                print("{}{}{}".format(i,j,k))

print(l)