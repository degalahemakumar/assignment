#Map Function:
#1.It is a built in function .used to apply a function to all the elements of the sequence(iterable).
#2.It assign a passed in function to all the elements present in an iterable objects and return a list.that contains a function call result.
#3.syntax:map(function,sequencevariable(or)iterable)
#Eg1:
def square(n):
    return n*n 
square(1)
square(2)
square(3)

#Eg2:
l1=[1,2,3]
def square():
    return l1*l1
print(square())
#output:TypeError: can't multiply sequence by non-int of type 'list'

#Eg3:
def square(n):
    return n*n 
l=[1,2,3]
print(list(map(square,l)))
#output:[1, 4, 9]

#Eg4:
l=[1,2,3,4,5]
print(list(map(lambda x:x*x,l)))
#output:[1, 4, 9, 16, 25]

#Eg5:
print(list(map(lambda x:x*x,range(1,6))))
#output:[1, 4, 9, 16, 25]

#Eg6:
print(list(map(lambda x:x%2==0,range(10))))
print(list(filter(lambda x:x%2==0,range(10))))
#output:
[True, False, True, False, True, False, True, False, True, False]
[0, 2, 4, 6, 8]

#Eg7:
print(list(map(lambda x:x*2,range(10))))  #works without condition
print(list(filter(lambda x:x+x,range(10)))) #works on condition thats y we not got addition values just printed range of x values
#output:
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Eg8:
a=[10,20]
b=(500,1000)
print(list(map(lambda x,y:x+y,a,b)))
#output:[510, 1020]

#Eg9:
s=['sai','kum','kinney']
print(list(map(lambda x:x,s)))
#output:['sai', 'kum', 'kinney']

#Eg10:
s=['sai','kum','kinney']
print(list(map(list,s)))
#output:[['s', 'a', 'i'], ['k', 'u', 'm'], ['k', 'i', 'n', 'n', 'e', 'y']]

