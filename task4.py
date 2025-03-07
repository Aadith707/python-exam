t="python is greate. python is easy. learning python is fun!"
freq={}
longword=""
uword={}
repword={}
for i in t.split():   
    n=t.count(i)
    freq[i]=n

    if len(i)>len(longword):
        longword=i

    for i,j in freq.items():
        if j==1:
            uword[i]=j

        else:
            repword[i]=j



        

print(freq)    
print("longest word:",longword)    
print("unique word:",uword.keys())
print("repeated word:",repword.keys())