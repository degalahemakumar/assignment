#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

a=(1, 2, 3, 4, 5, 6, 7, 8, 9)  
b=0
c=0
for x in a:
    if x%2==1:
        b+=1 
        print("even number form given is:",x)
print("count of even numbers form given is :",b)

for y in a:
    if y%2==1:
        c+=1 
        print("odd number form given is:",y)
print("count of odd numbers form given is :",c) 

#Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2 
a=input("enter any string value:") 
letters=0
digits=0 
for x in a:
    if x.isnumeric():
        digits+=1
print("total number of digits:",digits) 
for y in a:
    if y.isalpha(): 
        letters+=1 
print("total number of letters :",letters)

#Write a Python program that accepts a word from the user and reverses it    
user=input("enter user:") 
user_reverse=(user[::-1]) 
print(user_reverse) 

#Write a Python program to guess a number between 1 and 9.
number=int(input())  

if number>0 and number <10:
    print("well gussed") 
else:
    print("try again")