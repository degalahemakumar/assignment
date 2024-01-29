#Eg1:
def extra_work(f):
    def inner(x,y):
        if x%2==0 and y%2==0:
            f(x,y)
        else:
            print("please give both even numbers only") 
    return inner   
@extra_work
def sum(a,b):
    print(a+b)
sum(1,8)
#output:please give both even numbers only

#Eg2:
def extra_work(f):
    def inner(x,y):
        if x%2==0 and y%2==0:
            f(x,y)
        else:
            print("please give both even numbers only") 
    return inner   
@extra_work
def sum(a,b):
    print(a+b)
sum(4,8)
#output:12

#Eg3:
def extra_work(func):
    def inner(x,y):
        if x=="kinnera" and y=="saikumar":
            print("Your Details are matched")
            func(x,y)
        else:
            print("Invalid Details")
            print("Please try again")
    return inner
@extra_work
def full_name(firstname,lastname):
    print("First name:",firstname)
    print("Last name:",lastname)
a=input("Enter Your First Name:")
b=input("Enter Your Lasy Name:")
full_name(a,b)
#output:
#Enter Your First Name:kinnera
#Enter Your Lasy Name:saikumar
#Your Details are matched
#First name: kinnera
#Last name: saikumar

#output:
#Enter Your First Name:kinney
#Enter Your Lasy Name:sai
#Invalid Details
#Please try again

#Eg4:
def extra_work(full_name):
    def inner(firstname,lastname):
        if firstname=="kinnera" and lastname=="saikumar":
            print("Your Details are matched")
            full_name(firstname,lastname)
        else:
            print("Invalid Details")
            print("Please try again")
    return inner
@extra_work
def full_name(firstname,lastname):
    print("First name:",firstname)
    print("Last name:",lastname)
a=input("Enter Your First Name:")
b=input("Enter Your Lasy Name:")
full_name(a,b)
#output:
#Enter Your First Name:kinnera
#Enter Your Lasy Name:saikumar
#Your Details are matched
#First name: kinnera
#Last name: saikumar

#Eg5:
def extra_work(first):
    def inner():
        print("first i will excute because orginal function is connected with outer function so i m  excuted")
        first()
    return inner
@extra_work
def first():
    print('i will excute if given condition satifies the outer function which i m connected')
first()
#output:
#first i will excute because orginal function is connected with outer function so i m  excuted
#i will excute if given condition satifies the outer function which i m connected

#Eg6:
def extra_work(first):
    def inner():
        x=first()
        return x * x
    return inner
@extra_work
def first():
    return 10
print(first())
#output:100

#Eg7:
def extra_work(first):
    def inner():
        x=first()
        return x * x
    return inner
def other_extra(first):
    def inner_inner():
        y=first()
        return 2*y
    return inner_inner            
@extra_work
@other_extra
def first():
    return 10
print(first())
#output:400

#Eg8:
def extra_work(first):
    def inner():
        x=first()
        return x * x
    return inner
def other_extra(first):
    def inner_inner():
        y=first()
        return 2*y
    return inner_inner            
@other_extra                #which i give first that function will excute first
@extra_work                 #if i give second function first place it will excute only second one so give first function first place
def first():
    return 10
print(first())
#output:200

#Eg9:
def dec1(fname):
    def inner(name):
        print("first decor function execution")
        fname(name)
    return inner
def dec2(fname):
    def inner(name):
        print("second decor function execution")
        fname(name)
    return inner
@dec2
@dec1
def fname(name):
    print("hello ",name)
fname("sai")
#output:
#second decor function execution
#first decor function execution
#hello  sai

#Eg10:
def extra_work(f):
    def inner():
        f()
        return "i love my country"
    return inner
def other_extra(f):
    def inner_inner():
        f()
        return "with single photo maledivs GDP down fall"
    return inner_inner
@other_extra
@extra_work
def f():
    return "sai"
print(f())
#output:with single photo maledivs GDP down fall