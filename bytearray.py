#Empty bytearray:
a=[1,2,3,4,5,5,7,8,]
b=(71,72,73,74,74,75)
c={22,33,44,55,55,66}
d=bytearray(a)
e=bytearray(b)
f=bytearray(c)
print(type(d))
print(type(e))
print(type(f))
#Insertion is preserved and Duplicate objects are allowed:
print(*d)
print(*e)
#insertion is not preserved and Duplicate objects are not allowed:
print(*f)
#Hecterogeneous objects are not allowed alowed:
#Bytearray is mutable object:
d[0]=101
e[0]=101
f[0]=101
print(*d)
print(*e)
print(*f)
#Dynamic or growable are allowed: 
d.append(143)
e.append(143)
f.append(143)
d.remove(8)
e.remove(75)
f.remove(66)
print(*d)
print(*e)
print(*f)
#Indexing and Slicing are allowed:
print(d[0])
print(e[0])
print(f[0])
print(*d[::-1])
print(*e[::-1])
print(*f[::-1])