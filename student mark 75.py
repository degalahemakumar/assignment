n=int(input("enter number of student:"))
result={}
for i in range(0,n):
    print("enter of student no:",i+1)
    rno=int(input("Roll no:"))
    name=(input("Name:"))
    marks=int(input("Marks:"))
    result[rno]=[name,marks]
print(result)
for student in result:
    if result[student][1]>75:
        print(result[student][0])