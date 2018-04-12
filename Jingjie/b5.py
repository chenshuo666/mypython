import string
g=open('earthquake.json','r')
s=g.read()
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = {},space = {},digit = {},others = {}'.format(letters,space,digit,others))