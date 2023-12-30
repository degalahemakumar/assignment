a=int(input('enter the number of a:'))
b=int(input("enter the number of b:"))
l=[10,20,30,40,50,60]
try:
    c=a/b
    print(l[4])
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except :
    print("outer except block")
finally:
        print("outer finally block")


a=int(input('enter the number of a:'))
b=int(input("enter the number of b:"))
l=[10,20,30,40,50,60]
try:
    c=b/a
    print(l[4])
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except :
    print("outer except block")
finally:
        print("outer finally block") 

a=int(input('enter the number of a:'))
b=int(input("enter the number of b:"))
l=[10,20,30,40,50,60]
try:
    print(l[4])
    print("outer try block")
    try:
        print("inner try block")
        c=b/a
    except zerodivisionerror:
        print("inner except block")
    except valueerror:
         print("inner except block")
    finally:
        print("inner finally block")
except  :
    print("outer except block")
finally:
        print("outer finally block")         
