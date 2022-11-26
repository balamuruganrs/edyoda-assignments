b='Bala is A Handsome Boy'
u=0
d=0
for i in b:
    if i.isupper():
        u=u+1
    elif i.islower():
        d=d+1
print (u,d)
