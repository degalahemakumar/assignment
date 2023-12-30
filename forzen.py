x={} 
z=frozenset(x)
print(type(z))
y=set() 
m=frozenset(y)
print(type(m)) 
#print(x)
print(y)
#Insertion is not preserved:
a={1,2,3,4,5,5,6,"heamkumar",10.5,True,False}
b=frozenset(a)
print(b)
#Duplicate objects are not allowed:
print(b)
#Hecterogeneous objects are alowed:
print(b)
#frozenset is immutable object: 
#a[0]="kinnera"
#print(a)
#Dynamic or growable are not allowed:
#b.append('maruthi')
#b.remove('prasad')
#print(b)
#Indexing and Slicing are not allowed:
#print(a[0])                   
#print(a[::-1])
