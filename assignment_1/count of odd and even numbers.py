list=[1,2,3,4,5,6,7,8,9]
a=0
b=0
for i in list:
    if i%2==0:
        a=a+1
    else:
        b=b+1
print("total even numbers",a)
print("total odd numbers",b)
