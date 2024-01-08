#Filter Function:
#It is predefine function in python.The main objective of filter function to filter the data or information as per the application required
#it stores the the data or information inside the list data type,filter function can be applicable for namefull and nameless function.
#1.It is a built in function,used to filter out the elements of an iterator(sequence) depending on function that test each element in the sequence to be true or not.
#2.It return these elements of sequence for which function is true.
#3.syntax: filter(function_name,sequence variable)
#4.with base of condition filter function works and map function work without condition
#5.based on condition iterabale will filter
#6.without condition iterabales will map
#Eg1:
print('By using namefull function')      #BY using for loop also i can write even numbers 
def even_odd(num):                       #But filter function is built in function in python so it excute faster than forloop ,so we go with filter fumction
    if num%2==0:
        return True
    else:
        return False
num=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(even_odd,num))
print('The filter data is:',l1)
#output:
#By using namefull function
#The filter data is: [2, 4, 6, 8, 10]

#Eg2:
print('By using nameless function')
num=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda num:num%2==0,num))
print('The filter data is:',l1)
#output:
#By using nameless function
#The filter data is: [2, 4, 6, 8, 10]

#Eg3:
print(list(filter(lambda n:n%2==0,range(1,11))))
#output:[2,4,6,8,10]

#Eg4:
print(list(filter(lambda x:x>1000,range(1001,1005))))
#output:[1001,1002,1003,1004]

#Eg5:
i='saikumar'
print(list(filter(lambda x:x in ("aeiou"),i)))
#output:['a', 'i', 'u', 'a']

#Eg6:
i='saikumar'
print(list(filter(lambda x:x not in ("aeiou"),i)))
#output:['s', 'k', 'm', 'r']

#Eg7:
print(set(filter(lambda x:x==7,range(11))))
#output:{7}

#Eg8:
print(list(filter(lambda x:x%3==0,range(1,11))))
print(tuple(filter(lambda x:x%3==0,range(1,11))))
print(set(filter(lambda x:x%3==0,range(1,11))))
#output:
#[3, 6, 9]
#(3, 6, 9)
#{9, 3, 6}

#Eg9:
print(tuple(map(lambda x:x*3,range(1,11))))
print(set(filter(lambda x:x+3,range(1,11))))
#output:
#(3, 6, 9, 12, 15, 18, 21, 24, 27, 30) #map doest work on condition so we will get corrct output
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}       #in filter function it cant work because filter work on condition

#Eg10:
dic={1:'1',2:'2'}
print(dict(filter(lambda x:x[0]>=1,dic.items())))
#output:{1: '1', 2: '2'}
