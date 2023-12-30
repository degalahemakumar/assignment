'''a=int(input("enter the number of a:"))
   b=int(input("enter the number of b:"))
try:
    c=a/b
    print(c)
except:
    print("exception raised")
else:
    print("no exception")
finally:
    print("program end....")'''

'''try:
    amount=1999
    if amount<2999:
      raise valueerror ("please add money in your account")
    else:
     print ("you are eliglible to purchase product")
except valueerror as e:
      print(e) '''   
'''a=int(input("enter the number of a:")) 
b=int(input("enter the number of b:"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except:
    print("exception raised")'''
'''a=int(input("enter the number of a:"))
b=int(input("enter the number of b:"))
try:
    c=a/b
    print(c)
except exception as e:
    print(e)'''

'''a=int(input("enter the number of a:"))
b=int(input("enter the number of b:"))
l=[10,20,30,40,50,60]
try:
    c=a/b
    print(c)
    print(l[4])
except:
    b=1
    c=a/b
    print(c)'''

'''marks=1000
a=marks/0
print(a)'''

'''amount=1999
if amount>2999:
 print("your eligible to purchase product")'''
'''try:
    a=int(input("enter the number of a:"))
    b=int(input("enter the number of b:"))
    print(a/b)
except zerodivisionerror:
    print("cannot dividend by zero")
except valueerrorr: 
    print("please provide value not string ")'''

'''try:
    a=int(input("enter the number of a:"))
    b=int(input("enter the number of b:"))
    print(a/b)
except (zerodivisionerror, valueerrorr) as m:
    print(m) 
    print("please give valid value ")    '''
'''try:
    print("hi")
    print("10/0")
    print("hello")
except zerodivisionerror:
    print("state-4")
    print("state-5")'''
'''try:
    print("opening database")
    print(30/6)
    print("closing database")
except zerodivisionerror:
    print("handing code")
finally:
    print("closing the database")


try:
    print("outer try block")
    try:
        print("inner try block")
        print(20/0)
    except zerodivisionerror:
        print("inner except block")
    finally:
        print("inner finally block")
except :
    print("outer except block")
finally:
        print("outer finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(20/0)
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(20/0)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(20/0)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")'''
'''a=40
b=-20
try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(b/a)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")'''
'''a=40
b=-20
try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(b/a)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")       
'''
'''a=40
b=-20
try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("inner except block")
        print(a/b)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")'''

try:
    print("outer try block")
    try:
        print("inner try block")
    except zerodivisionerror:
        print("outer except block")
        print(20/0)
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except :
    print("outer except block")
finally:
        print("outer finally block")


try:
    print("outer try block")
    try:
        print("inner try block")
        print(b/a)
    except zerodivisionerror:
        print("inner except block")
    except indexerror:
         print("inner except block")
    finally:
        print("inner finally block")
except indexerror:
    print("outer except block")
finally:
        print("outer finally block")      