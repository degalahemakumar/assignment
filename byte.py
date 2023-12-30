
a=[1,2,3,4,5,5,7,8,]
b=(71,72,73,74,74,75)
c={22,33,44,55,55,66}
d=bytes(a)
e=bytes(b)
f=bytes(c)
print(type(d))
print(type(e))
print(type(f))
#Insertion is preserved and Duplicate objects are allowed:
print(*d)
print(*e)
#insertion is not preserved and Duplicate objects are not allowed:
print(*f)
#Hecterogeneous objects are not allowed alowed:
#Bytes is immutable object: so we cant replace values
#Dynamic or growable are not allowed: so we cant add or remove the values
#Indexing and Slicing are allowed:
print(d[0])
print(e[0])
print(f[0])
print(*d[::-1])
print(*e[::-1])
print(*f[::-1])
