
t=(x*x for x in range(10) if x%2==1)  
print(*t)

t=(x*x for x in range(10) if x%2==1)
print(t)
for i in t:
    print(i)

t=(x*x for x in range(10) if x%2==1)  
print(t)


#Eg2:
t=(x*x for x in range(10) if x%2==1) 
print(*t)
#output:1 9 25 49 81    