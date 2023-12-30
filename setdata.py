#x={} #set data type cant be empty if it is empty it is consider as dict data type
y=set() #use these method to for empty step 
#print(x)
print(y)
#Insertion is not preserved:
a={1,2,3,4,5,5,6,"kumar",10.5,True,False}
print(a)
#Duplicate objects are not allowed:
print(a)
#Hecterogeneous objects are alowed:
print(a)
#Set is mutable object: even though set is mutable we cant replace the values because insertion is not preserved
#a[0]="kinnera"
#print(a)
#Dynamic or growable are allowed:
a.add('hema')
a.remove('kumar')
print(a)
#Indexing and Slicing are not allowed:
#print(a[0])
#print(a[::-1])
