n=int (input("enter the number:")) 
for i in(range(0,n+1)):
    if i%2!=0:
        print(i)

#display only even number in between 0 to 300

n=int (input("enter the number:")) 
for i in(range(1,n+1)):
    if i%2==0:
        print(i) 

#take a list of number and print its sum 

number=[1,2,3,4,5]
total_sum=0 
for num in number:
    total_sum+=num 
print("sum of the number:",total_sum)

#take the range of number from 0 to 30 and print it sum  
n=int(input("enter the number:")) 
sum=0 
for i in range(1,n+1,1):
    sum=sum+i 
print("sum of first",n,"number is:",sum)