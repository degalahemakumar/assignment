a=10 
b=20
if a!=b:
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a") 
else:
    print("boths a and b are equal")

min =a 
if a:
    print(a<b)
else:
    b
print(min)

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 

min = a if a < b else b
print(min)

print( (b, a) [a < b] ) 

print({True: a, False: b} [a < b])

print((lambda: b, lambda: a)[a < b]()) 

a=5
b=7 
print(a,"is greater") if (a>b) else print(b,"is Greater") 

#special operators & identity (is & is not)
a = 10
b = 20
c = a
 
print(a is not b)
print(a is c) 

a = [1, 2, 3]
b = a
print(a is b)  
print(a is not b)  

x = 5
y = 10
print(x is y)  
print(x is not y)

#Membership operators (in & not in) 
text = "Hello, world!"
print("Hello" in text) 
print("hi" in text)  

fruits = ["apple", "banana", "cherry"]
print("grape" not in fruits)  
print("banana" not in fruits)  

a=(2,3,4,6,7,9,'pk','mp','mb')
print(1,10 not in a)

print("GFG") 
print('G', 'F', 'G')  
#string concatenate 
print('hema'+'-'+'degala'+'-'+'kumar') 
print('degala')
print() 
print('hello'+'kumar') 
print(2*'mp') 

# end and sep 
print('G', 'F', 'G', sep="#")
print("apple" + "-" + "banana" + "-" + "cherry") 
print("Apples", "Orange", "Mango", sep=", ", end=" 99999") 
print('hello ',end='') 
print('mp ',end="") 
print("pk ")

# input and output statements 

name = input("Enter your name: ") 
print("Hello, " + name)
print(type(name))

num = int(input("Enter a number: "))
add = num + 1
print(add) 

print(eval('1+2'))
print(eval("sum([1, 2, 3, 4])")) 

x = 5
print(eval('x == 4'))
x = None
print(eval('x is None')) 

expression = 'x*(x+1)*(x+2)'
print(expression)
x = 3
result = eval(expression) 
print(result) 

#.formating  

name = "Ram"
age = 22 
message = "My name is {0} and I am {1} year old. {1} is my favorat .number.".format(name, age)
print(message) 

str = "This article is written in {}"
print(str.format("Python")) 

print("Hello, I am {} years old !".format(18))  

print("Hi ! My name is {} and I am {} years old".format("User", 19))

print("This is {} {} {} {}".format("one", "two", "three", "four")) 

print("This site is {0:f}% securely {1}!!".format(100, "encrypted"))

# To limit the precision
print("My average of this {0} was {1:.2f}%".format("semester", 78.234876))
 
# For no decimal places
print("My average of this {0} was {1:.0f}%".format("semester", 78.234876))
 
# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}".format("binary", 100))
 
print("The {0} of 100 is {1:o}".format("octal", 100))

print("My average of this {0} was {1:.2f}".format("semester", 78.234876))