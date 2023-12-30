#t=()-------------->Valid
#t=tuple()--------->Valid
#t=10,20,30,40,50------->Valid
#t=10,20,30,40,50,------>Valid
#t=(10,20,30,40,50)----->Valid
#t=10,------------->Valid 
#t=(10,)----------->Valid
#t=10-------------->Invalid
#t=(10)------------>Invalid

#write 3 examples on each functions of tuple

a1=(20,9,8,'gmp',True,False) 
a2=(1,3,4,8,9)
y=a1+a2 
print(y)  

b1=(1,6,5.6,8+4,'mar')  
b2=(6,) 
z=b1+b2
print(z)
#b3=(6)
#print(b1+b2+b3) 

c1=(10,20,30,80,70)
c2=(20,40,30,50,60) 
x=c1+c2 
print(x)




d1=(1,20,3.5,'chiru',98,89,600,True)
a=d1*2 
print(a) 

#f1=(10,20,30,40,50,60,70) 
#f2=(20,3,8,4,6,9,'kumar',False)
#f=f1*f2
#print(f) 

#index()
g=(1,20,3.5,'chiru',98,89,600,True)  
print(g[0])

g1=(2,30,2.4,'bala',67,500,False) 
print(g1[5]) 

g3=(3,40,4.5,'nag',45,67,True,False) 
print(g3[7])

#count()

h=(9,68,2.3,123,'prakash',70,8+9,123,123,'cat')
print(h.count(123)) 

h1=(2,3,7,8,9.7,7.0,6,3,2,2,'ntr','ntr','2+3')
print(h1.count('ntr')) 

h2=(2,3,7,8,9.7,7.0,'dog',70,8+9,123,123)
print(h2.count(7))

#max()

i=(900,400,5000,8.9,300,500,8000)
print(max(i))

i1=('aman','chiru','bala','nag','ram') 
print(max(i1)) 

i2=(9.8,19,8,8000,60000,6.22)
print(max(i2))

#min() 
j=(10,7000,80.98,89,2,33,45)
print(min(j)) 

j1=('aman','chiru','bala','nag','ram') 
print(min(j1)) 

#sum()

k=(100,200,300,400,500)
print(sum(k))

k1=(100,400,500,20,40,59,10+20,10.5,)
print(sum(k1))

k2=(2,3,4,5)
k3=(6,7,8,9)
a=k2+k3
print(a)
print(sum(k3))

# len()
x1=(1,20,39,89,8.9,9,'hema',100,200,300)
print(len(x1))

y1=('gopi',2,3,8,9,39,7.8,True,False,8+2)
print(len(y1))

z1=(20,30,50,60,'abhi',3.4,400,10,'9+2') 
print(len(z1)) 


#shorted()

l=(2,309,40,500,700,900,509,2.98)
print(sorted(l))

l1=('aman','kumar','prasad','sai','kumar')
print(sorted(l1))

l2=(101,21,9,3,222,786,99)
print(sorted(l2))      
