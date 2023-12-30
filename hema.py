k=input("enter the name:")
count=0
for i in k:
    if i==('a') or i==('e') or i==('i') or i==('o') or i==('u'):
        count+=1
if count==0:
    print("no vowels are:")
else:
    print("vowels are:"+str(count))