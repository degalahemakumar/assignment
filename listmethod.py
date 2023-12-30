empty=[] 
list1=[24,'srh',87.6,45,8000,'kkr',45,82]
print(type(empty))
print(list1) 
print(empty)

list2=list()
print(type(list2))
print(list2)  

list3=[]
list3.append(20) 
list3.append(60)
list3.append(89) 
list3.append(69)
print(list3) 
print(type(list3))  


#list function

a1=[45,8.6,99,'book','89+2',78] 
print(list(a1)) 

a2=list(('car','bus','lorry','jeep','auto','bike')) 
print(a2)

a3='abcdefgh' 
string=list(a3) 
print(string)

#len function 

l=['hight',5.4,'weight',60,'body','rod','bus',6.9,56.7,'lorry']  
print(len(l)) 

e=['laptop',50000,'keybord',250,'charger',500,'mouse',980,564.6] 
print(len(e)) 

n=['number',30,'pattern',65.4,78+3,45,'56+4','khp','i+j'] 
print(len(n))  

#accessing of list 

b1=[30,7.8,123,78,'list','access',890]   
print(b1[5]) 

b2=[89,6.8,'nested','loop',[20,40,60],8,9]  
print(b2[4][1]) 

b3=[50,6.7,80+9,['gopi','kumar','sai','prakash'],78] 
print(b3[2])
print(b3[3][3])

#by using while and for loop  
#forloop  
# ex1
b=[34,89,98,6.7,89] 
for i in b:
    print(i)  

#ex2
    
name=[50,78,6.5,'loop',34] 
length=len(name) 
for i in range(length):
    print(name[i]) 

#ex3
word=['prasad','chiru','bala','nag']
for i in word:
    print(i)
  
#while loop 
    
n=10 
while n>0:
    print(n) 
    n-=1 
print("blast off")  

animal=['dog','cat','lion','fox','tiger']
i=0 
while i<len(animal):
  print(animal[i])
  i=i+1

frutites=['apple','bananna','orange','grepes']   
i=0 
while i<len(frutites):
    print(frutites[i]) 
    i+=1


#count()
co=[67,280,78.5,67,653,23,653,71,12,23,76,43] 
print(co.count(653)) 

u=[71,'shake',12.23,76,43,45,87,'hard',45,78,87,22,'people',45,33,'work',76,98,9]
print(u.count(45))

nt=['mango',65,2.3,5,'apple',567,'apple',34,'apple',567,'apple',876,980,234,567]  
print(nt.count('apple'))  


#index() 
i=['school',5,'zph',10,'inter',3,'beth',4,5.10,"3+4",1000,5.7] 
print(i.index(4))

nd=['python',3,'backend',7.8,900,654,20000,'langauge','tool',51,34,45,] 
print(nd.index(20000)) 

ex=[78,9.43,'srinu',654,20000,'prashnth',24,'python',5,'lerning']
print(ex.index(5)) 

#Diffrence b/w pop() and remove()
#remove()

#To delete value this method uses the value as a parameter.
#The remove() method doesn’t return any value.
#At a time it deletes only one value from the list 
#It throws value error in case of value doesn’t exist in the list.

#pop()
#This method also uses the index as a parameter to delete.
#pop() returns deleted value. 
#At a time it deletes only one value from the list.
#It throws index error in case of an index doesn’t exist in the list.

#append()

ap=[23,45,'append','insert',9.8] 
ap.append('mar') 
print(ap) 

my_work=[800,6.7,8+2,'pad'] 
my_work.append('member') 
print(my_work)

my_list1=[76,4.7,'word','cost',10] 
my_list2=[3.9,'name',8+3,78] 
my_list1.append (my_list2) 
print(my_list1)

#insert()

my_word=[10,20,309,78,'modal','jan','feb',3,5,673,21] 
my_word.insert(5,'box')
print(my_word)

mode=['dec',67,456,'mar',45.6,'A',23,145,65,78] 
mode.insert(10,'id:02470')
print(mode)

hard=[78.9,67.8,'true','false',54,97,123,354,'python',56+2,'speed',87654] 
hard.insert(6,8074061274) 
print(hard) 


#Extend() 

right1=['bala','nag',56,67.9,'chiru','venkey',23,53,459,765] 
right2=['cemera',90,'mobile']
right1.extend(right2)
print(right1)

left1=['ram',35,'ramcharn',34,'akhil',30,7,9,786] 
left2=[8908,874,23,4,'more','low','high'] 
left2.extend(left1)
print(left2)

middle1=['ysr',10,'tdp',60,'jsp',10,'98+1',67,543,764,9876] 
middle2=['grepes','mango','land','soil',65,87,678,432,867] 
middle2.extend(middle1) 
print(middle2)


#remove()
gold=[23.9,8,'car',9581701052,'raj','sky','ground',675,645,8074061274,87] 
gold.remove('ground')
print(gold)

tool=['cricket',67.8,98,'65+6',254,'highway',567,456,'park',54,765,987,100] 
tool.remove('65+6') 
print(tool)

type=['cat',8.5,67+4,98.9+6,'dog',24,67,'manu',23,65,75,11290,67.9]
type.remove(98.9+6)
print(type)

#pop()

hema=[45,9.9,'pk','kumar','45+2',78,80740,61274,'mohen'] 
print(hema.pop(7)) 
print(hema) 

mad=['james','chiru','ngk',34.5,89,'32+4',67,899,'word',98,7890]
print(mad.pop(5))
print(mad) 

surya=[2,3,4,9.9,'mango','apple','grepes',7890,564,764,]
print(surya.pop(5))
print(surya) 


#clear()

g=['mar',2470,890.0789,2465,'pavan',9.6,45,87]
print(g.clear()) 
print(g) 

m=['mp',34,5,6,'word','a',34,54] 
m.clear() 
print(m) 

p=['hema',7.9,23,4678,958,'kumar','gajula',78.9]
p.clear()
print(p) 

#reverse()
    
m=[123,45,67,9,'gopi',6,78,98,65]  
m.reverse() 
print(m)

k=[78,981,100,00,300,89,67,35]
k.reverse() 
print(k)

text=['gmp',67,78,98,67,9.78,564,789,456,'pk',7898,56]  
text.reverse()
print(text)  

word=['gopal','kumar','prakash','sai'] 
word.reverse() 
print(word)

#sort()

s=[29,9,585,6,9,67,56,54,65,69]  
s.sort() 
print(s)

pk=['Gopal','23+3','gmp','Mgp','kkr','sai','ak'] 
pk.sort() 
print(pk) 

mp=[345,789,98,78,8,23,45,13,65,45,56]
mp.sort() 
print(mp)