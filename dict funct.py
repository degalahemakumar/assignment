#Dictionary()
#insertion is preserved
#keys wont allow duplicate objects ,values allow duplicate objects
#hecterogenious objects allowed
#it is mutable object
#dynamic and growable not allowed
#indexing is allowed but slicing not allowed

#predefine functions for dict data type
#develop 3 programms using get() function
#Eg1:to get particular value from a set by using key we can call value as output
d={1:'a',2:'b',3:'c'}
c=d.get(2)
print(c)


#Eg2:
d={'apple':1,'ball':'cat',12.3:123}
c=d.get('apple')
print(c)


#Eg3
d={'apple':1,'ball':'cat',12.3:123}
c=d.get('cat')
print(c)


#develop 3 programms using len() function
#Eg1:to know the length of the dict() 
a={1:1,2:2,3:3,4:4,5:5}
print(len(a))
#output:5

#Eg2:
a={1:'as',2:'am',3:'un',4:'ur',5:1205,}
print(len(a))
#output:5

#Eg3:
a={1001:None,202:"sai",True:False,10.5:5}
b=len(a)
print(b)
#output:4

#develop 3 examples using pop() function()
#Eg1:to remove particular item from dict,but in set randomly it will remove
l={'s12':12.5,'':True}
l.pop('s12')
print(l)   
#output: {'': True}    

#Eg2:
l={set:float,12.5:'',True:False}
l.pop(set)
print(l)        
#output:{12.5: '', True: False}

#Eg3:
l={set:4,None:True}
l.pop(set)
print(l)
#output:{None: True}

#develop 3 programmes using keys() function
#Eg1:to display only keys
d={1:'a',2:'b',3:'c'}
c=d.keys()
print(c)
#output:dict_keys([1, 2, 3])

#Eg2:
d={'apple':1,'ball':'cat',12.3:123}
c=d.keys()
print(c)
#output:dict_keys(['apple', 'ball', 12.3])

#Eg3
d={'apple':1,'ball':'cat',12.3:123}
c=d.keys(1)
print(c)
#output:TypeError: dict.keys() takes no arguments (1 given)

#develop 3 programmes using values() function
#Eg1to display only values
l={'s12':12.5,'':True}
l.values()
print(l)   
#output: {'s12': 12.5, '': True}    

#Eg2:
l={set:float,12.5:'',True:False}
l.values()
print(l)        
#output:{<class 'set'>: <class 'float'>, 12.5: '', True: False}

#Eg3:
l={set:4,None:True}
l.values()
print(l)
#output:{<class 'set'>: 4, None: True}

#develop 3 programmes using items() function
#Eg1:to display both keys and values
a={'x':1,'y':55,'z':786}
c=a.items()
print(c)
#output:dict_items([('x', 1), ('y', 55), ('z', 786)])

#Eg2:
a={'sai':'kum','kinney':'sai','kum':'kiney'}
c=a.items()
print(c)
#output:dict_items([('sai', 'kum'), ('kinney', 'sai'), ('kum', 'kiney')])

#Eg3:
a={1:1,4:2,44:3,55:44}
c=a.values()
print(c)
#output:dict_values([1, 2, 3, 44])

#develop 3 programms using copy() function
#Eg1:to copy total dict
d={1:'a',2:'b',3:'c'}
c=d.copy()
print(c)
#output:{1: 'a', 2: 'b', 3: 'c'}

#Eg2:
d={'apple':1,'ball':'cat',12.3:123}
c=d.copy()
print(c)
#output:{'apple': 1, 'ball': 'cat', 12.3: 123}

#Eg3
d={'apple':1,'ball':'cat',12.3:123}
c=d.copy("apple")
print(c)
#output:TypeError: dict.copy() takes no arguments (1 given)

#develop 3 examples using del() function
#Eg1: to delete particular item by giving particular key
d={'apple':1,'ball':'cat',12.3:123}
del d['ball']
print(d)
#output:{'apple': 1, 12.3: 123}

#Eg2:
d={'apple':1,'ball':'cat',12.3:123}
del d[1]
print(d)
#output:KeyError: 1    {we cant del using values by using only keys we can del}

#Eg3:
d={set:dict,True:False,int:str}
del d[int]
print(d)
#output:{<class 'set'>: <class 'dict'>, True: False}

#develop 3 programmes using setdefault() function
#Eg1:to create a default item into dict which can be used as it setdefault
s={True:False,"s":1,12.4:44}
a=s.setdefault('s',22)               #in dict key cant be same ,values can be same 
print(a)                             #so we cant setdefault using same key
print(s)
#output:1  {True: False, 's': 1, 12.4: 44}                             

#Eg2:
s={True:False,"s":1,12.4:44}
a=s.setdefault('st',200)
print(a)
print(s)
#output:200  {True: False, 's': 1, 12.4: 44, 'st': 200}

#Eg3:
s={True:False,"s":1,12.4:44}
a=s.setdefault('b',1)
print(a)
print(s)
#output:1   {True: False, 's': 1, 12.4: 44, 'b': 1}

#dict() comprehension
#Eg1:
d={x:x for x in range(10)}
print(d)
#output:{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

#Eg2:
d={x:x^x for x in range(10)}
print(d)
#output:{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

#Eg3:
d={x:x**x for x in range(10) if x%2==1}
print(d)
#output:{1: 1, 3: 27, 5: 3125, 7: 823543, 9: 387420489}