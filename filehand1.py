f=open('abc.txt','r')
line1=f.readline()
while line1 !=" ":
 print(line1,end=" ")
 line1=f.readline()
f.close()

f=open('abc.txt','r')
line1=f.readline()
while true :
 print(line1,end=" ")
 line1=f.readline()
f.close()

f1=open('input.txt','r')
f2=open('output.txt','w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()
print('data copied from input file to output file successfully')