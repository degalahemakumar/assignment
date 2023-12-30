x=[[115,125,135,145],[165,175,185,195],[110,115,125,135],[145,155,165,175]] 
for i in range(len(x)): 
    for j in range(len(x[i])): 
        print(x[i][j],end="  ") 
    print() 


#----------------------------

 
y=[[115,125,135,145,155],[110,210,310,410,510],[145,155,165,175,145],[675,876,987,456,876],[212,213,214,215,216]]   

for i in range(len(y)): 
    for j in range(len(y[i])): 
        print(y[i][j],end="  ") 
    print()  

#--------------------------------- 
    
z=[[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,38,40],[41,42,43,44,45,46,47,48,49,50]] 

for i in range(len(z)): 
    for j in range(len(z[i])): 
        print(z[i][j],end="  ") 
    print()  

#List comprehensions  
    
#words= ["aman",naga","chandra","chiru"]
#expected output: ["a","m","a","n"] 
#by using list comprehensive method only     
words= ["aman","naga","chandra","chiru",]   

words=[words for i in ["aman","naga","chiru","chandra",] for words in i if i=="aman"] 
print(words)
        

#s="the birds on the tree has no feathers but still it trys to fly in the sky"  
#you have to convert this sentance by list comprehensive  

s="the birds on the tree has no feathers but still it trys to fly in the sky"  
#s=input("enter string:")
y = print([ch.upper()for ch in s])
print(y)

l=s.upper() 
print(l)  

#write a pr to display unique vowels present in the given word(given word should be taken from key board)
s="the birds on the tree has no feathers but still it trys to fly in the sky"  
#Eg1:
s=input("Enter any string:")
c=0
for x in s:
    if x in ("aeiouAEIOU"):
        c+=1
        print(x,"is an vowel")
print("number of vowels in given string is:",c) 


n= input('Enter any string : ')
for ch in n:
  if ch in 'aeiouAEIOU':
    print(ch)