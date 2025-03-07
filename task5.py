sentence = "madam and racecar are level racecar madam"

d={}
for i in sentence.split():

    d[i]={
        "length":len(i),
        "palindrom":i==i[::-1],
        "count":sentence.count(i)

    }   

print(d,end=" ") 
print()    


