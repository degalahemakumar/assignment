#set()
#insertion is not preserved
#dyplicate objects are not allowed
#hectergenious objects are allowed
#set is mutable
#dynamic and growable are allowed
#indexing and slicing are not allowed

#predefine functions for set data type:
#write 3 examples using add() function for set()
#Eg1: adding new items into a set
a={1,2,3,4}
a.add("sai")
print(a)
print(type(a))
#output:{1, 2, 3, 4, 'sai'} <class 'set'>

#Eg2:
a={1,"sai","sai",10.5,True,None}
a.add(False)
print(a)
#output:{None, 1, False, 10.5, 'sai'}

#Eg3:
a={1,}
a.add("ten")
print(a)
#output:{1, 'ten'}

#develop 3 programms using len() function
#Eg1:to know the length of the a set
a={1,2,3,4,5}
print(len(a))
#output:5

#Eg2:
a={1,2,3,4,5,}
print(len(a))
#output:5

#Eg3:
a={1001,202,"sai",True,10.5}
b=len(a)
print(b)
#output:5

#write 3 examples using clear function using list:
#Eg1:to clear total set
l={int,float,str,bool,complex}
l.clear()
print(l)
#output:set()

#Eg2:
l={int,float,str,bool,complex}
l2={}
l2.clear()
print(l2)
#output:{}

#Eg3:
l={}
l2={1,2,3,4,}
l2.update(l)
l.clear()
print(l) 
#output:{}

#write 3 examples using pop function from list:
#Eg1:to delet the random item from a set 
l={'s12',12.5,'',True}
l.pop()
print(l)   
#output:{True, 's12', 12.5}     

#Eg2:
l={set,12.5,'',True}
l.pop()
print(l)        
#output:{<class 'set'>, 12.5, True}

#Eg3:
l={set,4,76,'',True}
l.pop()
print(l)
#output:{<class 'set'>, True, 4, 76}

#develop 3 programms using update() function
#Eg1:to update the values into a set
s={"sai",'kinney','''val'''}
s.update("""will""")
print(s)
#output:{'l', 'i', 'sai', 'w', 'kinney', 'val'}

#Eg2:
s={"!@#$%^&&"}
s.update("?")
print(s)
#output:{'!@#$%^&&', '?'}

#Eg3:
s={"a",'b','c','d'}
s.update('e')
print(s)
#output:{'e', 'b', 'd', 'c', 'a'}

#develop 3 examples using copy() function:
#Eg1:to copy a set
s=set()
s.update("sai")
print(s)
s.clear()
print(s)
s.copy()
print(s)
#output:{'a', 's', 'i'} set() set()

#Eg2:
s={set,complex,int,float}
s.copy()
print(s)
#output:{<class 'set'>, <class 'float'>, <class 'complex'>, <class 'int'>}

#Eg3:
s={[1,2,3],[3,4,5]}
s.copy()
print(s)
#output:TypeError: unhashable type: 'list'

#write 3 examples on remove() function:
#Eg1:to remove particular item from a set
s={'iam','youare'}
s.remove('iam')
print(s)
#output:{'youare'}

#Eg2:
s={'!','@','#','%'}
s.remove()
print(s)
#output:TypeError: set.remove() takes exactly one argument (0 given)

#Eg3:
s={{1},{2},{3}}
s.remove(2)
print(s)
#output:TypeError: unhashable type: 'set'

#Eg4:
s={'!','@','#','%'}
s.remove('&')
print(s)
#output:KeyError: '&'

#develop any 3 programms using discard() function
#Eg1:it removes particular item same as remove but when we give value which is not there in set ,then also it will give output with excting values
s={'a','b','c'}
s.discard('b')
print(s)
#output:{'a', 'c'}

#Eg2:
s={1,2,3,4,False}
s.discard()
print(s)
#output:TypeError: set.discard() takes exactly one argument (0 given)

#Eg2:
s={1,2,3,4,False}
s.discard(None)
print(s)
#output:{False, 1, 2, 3, 4}

#develop 3 programes using union() function  symbol{|}
#Eg1:to combine two sets into single set by removing duplicate objects
a={'a','b','c'}
b={'d','a','g'}
c=a.union(b)
print(c)
#output:{'c', 'b', 'd', 'a', 'g'}

#Eg2:
a={1,2,3,4,44,}
b={55,66.77}
c=a.union(b)
print(c)
#output:{1, 2, 3, 4, 66.77, 55, 44}

#Eg3:
a={'a','b','c'}
b={'d','a','g'}
c=a|(b)
print(c)
#output:{'d', 'b', 'c', 'g', 'a'}

#develop 3 examples using intersection() function  symbol{&}
#Eg1:it will display the commen values present b/w two sets
x={'apple','ball','cheery'}
y={'goa','banana','ball'}
z=x.intersection(y)
print(z)
#output:{'ball'}

#Eg2:
x={'apple','ball','cheery'}
y={'goa','banana','ball'}
z=x&(y)
print(z)
#output:{'ball'}

#Eg3:
s={1,2,3,4,5}
b={1,2,3,4}
z=s&(b)
print(z)
#output:{1, 2, 3, 4}

#develop 3 programms using difference() function  symbol{-}
#Eg1:it will display the diiferent values which are not commen
a={'x','y','z'}
b={'z','a','b'}
c=a.difference(b)
print(c)
#output:{'y', 'x'}

#Eg2:
a={'sai','kinney','kum'}
b={'kum','sai','kiney'}
c=a.difference(b)
print(c)
#output:{'kinney'}

#Eg3:
a={1,4,44,55,66}
b={1,2,3,44,}
c=a-(b)
print(c)
#output:{66, 4, 55}

#develop 3 programms using symmetric_difference() function     symbol{^}
#Eg1:it will show the items which is not present in sets
s={'apple','banana','cherry'}
t={'anapple','banana','cat'}
z=s.symmetric_difference(t)
print(z)
#output:{'cherry', 'cat', 'apple', 'anapple'}

#Eg2:
s={'apple','banana','cherry'}
t={'anapple','banana','cat'}
z=s^(t)
print(z)
#output:{'cherry', 'cat', 'apple', 'anapple'}

#Eg3:
a={'a','b','c'}
b={'d','a','g'}
c=a^(b)
print(c)
#output:{'b', 'g', 'c', 'd'}

#set() comprehension
#Eg1:
s={x for x in range(10)}
print(s)
#output:{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#Eg2:
s={x for x in range(10) if x%2==1}
print(s)
#output:{1, 3, 5, 7, 9}

#Eg3:
s={x*3 for x in range(10) if x%2==1}
print(s)
#output:{3, 9, 15, 21, 27}