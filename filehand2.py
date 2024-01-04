f1=open('sunrise.jpg','rb')
f2=open('new-sunrise.jpg','wb')
b=f1.read()
f2.write(b)
print(f2)

import csv

with open("emp.csv",'w',newline='') as a:
    w=csv.writer(a)
    w.writerow(["emp_id","emp_name",'emp_phn'])
    n=int(input("enter number of employee to entry details "))
    for i in range(1,n+1):
        print(i," EMPLOYEE DEATILS ")
        eid=int(input("enter employee no : "))
        ename=input("enter the emp name :")
        ephn=input("enter the emp phn :")
        w.writerow([eid,ename,ephn])
    print("totsl emp data written to csv file ")


    import csv

with open("emp.csv",'w',newline='') as a:
    w=csv.writer(a)
    w.writerow(["emp_id","emp_name",'emp_phn'])
    n=int(input("enter number of employee to entry details "))
    for i in range(1,n+1):
        eid=int(input("enter employee no : "))
        ename=input("enter the emp name :")
        ephn=input("enter the emp phn :")
        print(i," EMPLOYEE DEATILS ")
        w.writerow([eid,ename,ephn])
    print("totsl emp data written to csv file ")

import csv
f=open('emp.csv','r')
r=csv.reader(f)
d=list(r)
print(d)
for i in d:
    for w in l:
        print(w,"________._._._",end="")
print()   

f=open("abc.txt",'r')
print(f.tell)
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())

data="all student are good"
f=open("abc.txt",'w')
f.write(data)
with open("abc.txt","rt") as f:
    text=f.read()
    print(text)
    print("the current cursor position:",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("data after modiflication:")
    print(text)

f=open("hero.txt","w")
f=open("villian.txt","w")
f=open("director.txt","w")


from zipfile import*
f=ZipFile("file.zip","w")
f.write("hero.text")
f.write("villian.txt")
f.write("director.txt")
f.close()
print("zip file created")


from zipfile import*
f=ZipFile("file.zip","w")
f.write("hero.text")
f.write("villian.txt")
f.write("director.txt")
f.write('emp.csv')
f.close()
print("zip file created")


from zipfile import*
f=ZipFile("file.zip","w")
f.write("hero.text")
f.write("villian.txt")
f.write("director.txt")
f.write('emp.csv')
f.close()
print("zip file created")
for i in names:
    print("file name is",i)


    from zipfile import*
f=ZipFile("file.zip","w")
f.write("hero.text")
f.write("villian.txt")
f.write("director.txt")
f.write('emp.csv')
f.close()
print("zip file created")
for i in names:
    print("file name is",i)
    f1=open(i,"r")
    print(f1.read())
    print()