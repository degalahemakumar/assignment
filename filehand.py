
f=open('abe.txt','w')
print('name:',f.name)
print('mode:',f.mode)
print('closed:',f.closed)
print('readable:',f.readable())
print('written:',f.written())


f=open('abe.txt','w')
print('name:',f.name)
print('mode:',f.mode)
print('closed:',f.closed)
print('readable:',f.readable())
print('written:',f.written())
f.close()
print('fileclosed:',f.close())


f=open('abc.txt','w')
f.write('degala')
f.write('hema')
f.write('kumar')
print('data written to file successfully')
f.close ()

f=open('abc.txt','w')
f.write('degala')
f.write('hema\n')
f.write('kumar\n')
print('data written to file successfully')
f.close ()

f=open('abc.txt','w')
list=['sunny','hema','kumar','prakesh']
f.writelines(list)
print('all lines from the list nwritten to the list')
f.close()

f=open('abc.txt','w')
list=['sunny\n','hema\n','kumar\n','prakesh\n']
f.writelines(list)
print('all lines from the list nwritten to the list')
f.close()


f=open('abc.txt','r')
data=f.read()
print(data)
f.close()

f=open('abc.txt','r')
data=f.read(10)
print(data)
f.close()

f=open('abc.txt','r')
line1=f.readline()
print('line1()',end=" ")
line2=f.readline()
print('line2()',end=" ")
line3=f.readline()
print('line3()',end=" ")
f.close()

f=open('abc.txt','r')
line1=f.readline()
print('first number:',line1,end=" ")
line2=f.readline()
print('seconed number:',line2,end=" ")
line3=f.readline()
print('third number:',line3,end=" ")
f.close()

f=open('abc.txt','r')
lines=f.readlines()
for line in lines:
    print(line,end=" ")
    f.close()

f=open('abc.txt','r')
print(f.read(3))
print( f.readline ())
print(f.readline())
print(f.read(4))
print("remaining data")
print(f.read()) 

with open("abc.txt","w") as f:
 f.write("sunny")
 f.write("hema\n")
 f.write("kumar\n")
 print("flie closed",f.closed)
 print("flie closed:",f.closed)

with open("abc.txt","w") as f:
 f.write("sunny")
 f.write("hema\n")
 f.write("kumar\n")
 print("flie closed\n",f.closed)
 print("flie closed:",f.closed)

f=open('abc.txt','r')
line1=f.readline()
while line!="":
 print(line1,end=" ")
 line1=f.readline()
f.close()

f=open('abc.txt','r')
line1=f.readline()
while true:
 print(line1,end=" ")
 line1=f.readline()
f.close()