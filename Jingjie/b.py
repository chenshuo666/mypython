a={'e':543,'r':664}
b={'w':78,'g':56}

d=list(a.values())
d1=list(b.values())
d.extend(d1)
print('%d'% d)
