# 1 right downword traingle
n=int(input("enter number:")) 
for i in range(n):
    print((chr(65+i)+" ")*(n-i))  

n=int(input("enter number:")) 
for i in range(n):
    print((str(i+1)+" ")*(n-i)) 

n=int(input("enter number:")) 
for i in range(n):
    print(("* ")*(n-i))  

# pyramid pattern

n=int(input("enter number:")) 
for i in range(n):
    print(" "(n-i-1)+" "*(i+1))

n=int(input("enter number:")) 
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print()

n=int(input("enter number:")) 
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

# right triangle
n=int(input("enter number:"))
for i in range(1, 6):
    for j in range(1 , i + 1):
        print(j , end=' ')
    print()  

n=int(input("enter number:"))
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(ord('a') + j - 1),end=' ')
    print()  

n=int(input("enter number:"))
for i in range(1, 6):
    for j in range(i):
        print('* ', end='')
    print()  

# Diamond pattern

num=int(input("Enter a number:")) 
for i in range(1,num+1): 
    print(" "*(num-i),end="") 
    for j in range(1,i+1): 
        print("*",end=" ") 
    print() 
for p in range(1,num): 
    print(" "*p,end="") 
    for q in range(1,num+1-p):
        print("* ",end="")
    print()

num=int(input("Enter a number:")) 
for i in range(1,num+1): 
    print(" "*(num-i),end=" ") 
    for j in range(1,i+1): 
       print(j,end=" ") 
    print() 
for p in range(1,num): 
    print(" "*p,end=" ") 
    for q in range(1,num+1-p):
        print(q,end=" ")
    print() 


num=int(input("Enter a number:")) 
for i in range(1,num+1): 
    print(" "*(num-i),end=" ") 
    for j in range(1,i+1): 
       print(chr(64+i),end=" ") 
    print() 
for p in range(1,num): 
    print(" "*p,end=" ") 
    for q in range(1,num+1-p): 
       print(chr(64+num-p),end=" ")
    print() 

#reverse pyramid

num=int(input("Enter a number:")) 
for i in range(1,num+1): 
   print(" "*(i-1),end="") 
   for j in range(1,num+2-i): 
       print("*",end="") 
   for k in range(1,num+1-i): 
       print("*",end="")
   print()
   
num=int(input("Enter a number:")) 
for i in range(1,num+1): 
    print(" "*(i-1),end="") 
    for j in range(0,num+1-i): 
        print(num+1-i,end="") 
    for k in range(1,num+1-i): 
        print(num+1-i,end="") 
    print() 
    
num=int(input("Enter a number:")) 
for i in range(1,num+1): 
    print(" "*(i-1),end="") 
    for j in range(1,num+2-i): 
        print(chr(65+num-i),end="") 
    for k in range(2,num+2-i): 
        print(chr(65+num-i),end="")
    print()

# left pascal's tariangle

n=int(input("Enter a number:")) 
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(chr(65+n-i),end=" ") 
    print() 
for a in range(1,n+1): 
    for k in range(0,n-a): 
        print(chr(65+a),end=" ") 
    print() 

n=int(input("Enter a number:")) 
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(n-i+j-1,end=" ") 
    print() 
for a in range(1,n+1): 
    for k in range(0,n-a): 
        print(k+a,end=" ") 
    print() 

n=int(input("Enter a number:")) 
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print("*",end=" ") 
    print() 
for a in range(1,n+1): 
    for k in range(1,n+1-a): 
        print("*",end=" ")
    print()  

#left triangle

n=int(input("Enter a number:"))
for i in range(1, n):
    num = 1
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("") 


n=int(input("Enter a number:"))
k = 2 * n - 2
for i in range(0, n):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("") 




# left downward triangle star pattern
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n, i, -1):
        print("*", end=" ")
    print() 

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" " *(i-1),end="  ")
    for j in range(65,66+n-i):
        print(chr(j),end="") 
    print()

n=int(input("Enter a number:"))
for k in range(0, n):
    for m in range(n-1, k-1):
        print(m, end=" ")
    for j in range(k):
        print(' ', end=" ")
    for h in range(k + 1, n):
        print(h, end=" ")
    print()

# right Pascals Number Pattern
n=int(input("Enter a number:"))
for i in range(1, n + 1):
    for j in range(i, n):
        print(end = '  ')
    for k in range(1, i + 1):
        print(k, end = ' ')
    print()
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(end = '  ')
    for k in range(1, i):
        print(k, end = ' ')
    print() 

n=int(input("Enter a number:"))
for i in range(n):
    print("  "(n-i-1)+(str(i+1)+" ")(i+1)) 
for i in range(n-1):
    print("  "(i+1)+(str(n-i-1)+" ")(n-i-1))


n=int(input("Enter a number:"))
i = 1
while i <= n:
    j = i
    while j < n:
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1
i = n
while i >= 1:
    j = i
    while j <= n:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1     

#square pattern
n=int(input("Enter a number:"))
for i in range(0, n):
    for j in range(0, n):
        print("*", end="")
    print() 
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        print(j+1, end=' ')
    print()

n=int(input("Enter a number:"))

for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()