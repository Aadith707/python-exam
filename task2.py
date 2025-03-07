l=[2,25,765,24,111]
sum=[]
for i in l:
    s=0
    for j in str(i):
        s=s+int(j)
    sum.append(s)

print(sum)        
