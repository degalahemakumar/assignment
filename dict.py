d={}
print(d)
d[100,200]= 'hema','kumar'
print(d)
l={100:'kumar',200:'hema',400:'shiva'}
print(l)
l[100]='pavan'
print(l)
l[100,200]='pavan','omkar'
del l[100]
print(d)
l={100:'kumar',200:'hema',400:'shiva'}
del l[100]
print(l)
l={100:'kumar',200:'hema',400:'shiva'}
l.clear()
l[100]='omkar'
print(l)
b={'hema','kumar','degala'}
d={100:b}
print(d)
d={100:'shiva'}
print(d)
b=['hema','kumar','degala']
d={100:b}
print(d)
d=dict()
print(d)
d=dict([(10,'hi'),(20,'hello'),(30,'okay')])
print(d)
d=dict([(30,'priya')])
print(d)
d[30]='hema'
print(d)
d[40]='etv'
print(d)
print(len(d))
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
print(d.get(200))
print(d.get(30))
print(d.get(20,10))
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
print(d.pop(20))
print(d.pop(10))
print(d.pop(30,10))
print(d)
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
print(d.popitem())
print(d.popitem())
print(d.popitem())
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
print(d.keys())
print(d.values())
print(d.items())
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
l=d.items()
print(l)

for k,v in l:
    print("keys are",k,"valuesare",v)
d=dict([(10,'etv'),(20,'star maa'),(30,'gemini')])
a=d.keys()
b=d.values()
for x in a:
    print(x)
    for y in b:
        print(y)
d=dict([(10,'etv'),(20,'starmaa'),(30,'gemini')])
a=d.keys()
b=d.values()
for x in a:
    print(x, end=" ")
for y in b:
     print(y, end=" ")