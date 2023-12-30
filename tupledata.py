x=[]
y=tuple()
print(x)
print(y)
#Insertion is preserved:
a=(1,2,3,4,7,5,6,"hemakumar",10.5,True,False)
print(a)
#Duplicate objects are allowed:
print(a)
#Hecterogeneous objects are alowed:
print(a)
#Tuple is immutable object: so we cant replace the values in tuple
#a[0]="kinnera"
#print(a)
#Dynamic or growable are allowed:so we cant add or remove the valuse because tuple is immutable
#a.append('prasad')
#a.remove('maruthi')
#print(a)
#Indexing and Slicing are allowed:
print(a[0])
print(a[::-1]) 
