l=[(3,5),(1,1),(4,3),(7,2)]

for i in range (len(l)):
    for j in range(len(l)):
        if l[i][1]<l[j][1]:
            l[i],l[j]=l[j],l[i]
print(l)
