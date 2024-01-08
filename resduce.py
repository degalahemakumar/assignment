#1.This function is used to reduce a sequance of elements to a single value by processing the elements according to a function supplied
#2.It returns a single value 
#3.This funcation is a part of functiontools module ,so you have to import it before using
#4.syntax:from functools import reduce
#         reduce(function_name,sequence(or)iterable)
#the main object of reduce function to reduce iterables into single entity like sum of list ,sum of first 100 numbers
#Eg1:sum of first 10 natural numbers(we can do with forloop also but reduce function is faster then the forloop)
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,l))
#output:55

#Eg2:
from functools import reduce
print(reduce(lambda x,y:x+y,range(1,11)))
#output:55

#Eg3:
from functools import reduce
def fun(x,y):
    return x*y
print(reduce(fun,[1,2,3,4,5]))
#output:120

#Eg4:
from functools import reduce
def fun(x,y):
    return x*y
print(reduce(fun,[]))
#output:TypeError: reduce() of empty iterable with no initial value

#Eg5:
from functools import reduce
def fun(x,y):
    return x if x>y else y
def fun1(x,y):
    return x if x<y else y
a=reduce(fun,[1,2,3,4,5])
b=reduce(fun1,range(1,6))
print('maximum value is:',a)
print('minimum value value is:',b)
#output:
#maximum value is: 5
#minimum value value is: 1

#Eg6:
from functools import reduce
def boo(a,b):
    return bool(a and b)
print(reduce(boo,[1,1,1,1,1]))
print(reduce(boo,[1,1,1,1,0]))
#output:
#True
#False

#Eg7:
from functools import reduce
def boo(a,b):
    return bool(a or b)
print(reduce(boo,[1,1,1,1,1,]))
print(reduce(boo,[0,0,0]))
#output:
#True
#False

#Eg8:
from functools import reduce
a=[[1,2,3],[4,5,6],[7,8,9]]
print(reduce(lambda x,y:x+y,a))
#output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Eg9:
from functools import reduce
a=[1,4,8,18,22]
print(reduce(lambda x,y:x+y,a,3))
#output:56

#Eg10:
from functools import reduce
print(reduce(lambda x,y:x+y,range(10),5))
#output:50