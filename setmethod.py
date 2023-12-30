a=['sachin','sai','lol','nagi','kittu']
for x in a:
    print(x,',',end=' ')
print("others are best friends") 

#Eg1:
a=['sachin','sai','lol','nagi','kittu']
x=" ,".join(a)
print(x,"are friends")   

#Eg2:
a=('sachin','sai','lol','nagi','kittu')
x=" ,".join(a)
print(x,"are friends")   

#Eg3: insertion is not preserved so it will get zig zag
a={'sachin','sai','lol','nagi','kittu'}
x=" ,".join(a)
print(x,"are friends") 

#Eg4:
a=['will','you','love','me']
x=" ".join(a)
print(x, "jai")   

#write 3 programms using upper() function
#upper function cant used in list ,tuple and set
#Eg1:
a='can you change me lower case to upper case'
b=a.upper()
print(b)  

#Eg2:
a='AZMA is our HR,Please ping her any issue'
b=a.upper()
print(b)   

#Eg3: it will convert only lower alphabets into upper alphabets
a='#$%^&*1234567'
b=a.upper()
print(b) 


#write 3 programms using lower() function
#lower function cant used in list ,tuple and set
#Eg1:
a="YES I AM WORKING AS PYTHON DEVELOPER"
print(a.lower())

#Eg2:
a="YES man I like it"
print(a.lower())

#Eg3:
a='#$%^&*1234567'
b=a.lower()
print(b)

#write 3 programms using swapcase() function  #convert lowercase to upper and uppercase to lower
#does not support list,tuple,set
#Eg1:
a="YES man I like it"
print(a.swapcase())

#Eg2:
a=input("enter any string:")
print(a.swapcase())

#Eg3:
a="fsjgdebwbc 1234#$$%"
print(a.swapcase())

#write 3 programmes using title() function  #every string value of staring alphabet will be upper case
#Eg1:
a="hai man, how are you!"
print(a.title())

#Eg2:
a="hai man, how are you! i am 22years"
print(a.title())

#Eg3:
a="please tell me your id? m22m22m22"
print(a.title())

#write 3 examples using capitalize() function  #only stating letter of string will be uppercase
#Eg1:
a="please tell me your id? m22m22m22"
print(a.capitalize())

#Eg2: we wont get output because 'p' is not staring letter of string
a="#$% please tell me your id? m22m22m22"
print(a.capitalize())

#Eg3: we wont get total "PLEASE" and "YOUR" in capital,only staring string 'P' will be same and remaing all capital convert into lower case
a="PLEASE tell me YOUR id? m22m22m22"
print(a.capitalize())


#write 3 programmes using isalnum() function
#it will check in given string has only alnum values or not there by using boolean value
#Eg1: output:False because we have spaces between every alpha string so space is not alnum
a="i wont print anything like 2234"
print(a.isalnum())

#Eg2:output:True
a="hemakumar786"
print(a.isalnum())

#Eg3: output:Falsee
a="hemakumar786"
print(a.isalnum())


#write 3 programmes using isalpha() function
#it will check in given string total alphabets there or not there
#Eg1:
a="HEMAKUMARsaikumar"
print(a.isalpha())

#Eg2:
a="HEMAKUMARsaikumar123"
print(a.isalpha())

#Eg3:output:Flase because in string contains spaces
a="HEMAKUMAR i not good as u think"
print(a.isalpha())

#write 3 programmes using isdigit() function
#it will check in given string total digits there or not there
#Eg1:
a="1,2,3,4,56"
print(a.isdigit())

#Eg2:output:True
a="123"
print(a.isdigit())

#Eg3:output:Flase because in string contains spaces and alpha string
a="HEMAKUMAR 1i2not good as u think"
print(a.isdigit())


#write 3 programmes using islower() function
#it will check in given string total lowercase there or not there
#Eg1:output:True
a="i am kumar untill u call me bro"
print(a.islower())

#Eg2:output:True
a="yes123"
print(a.islower())

#Eg3:output:False
a="HEMAKUMAR1i2not good as u think"
print(a.islower())


#write 3 programmes using isupper() function
#it will check in given string total uppercase there or not there
#Eg1:
a="i am hema untill u call me bro"
b=a.upper()
print(b.isupper())

#Eg2:
a="yes123"
print(a.isupper())

#Eg3:
a="HEMAKUMAR1i2not good as u think"
print(a.isupper())


#write 3 programmes using istitle() function
#it will check in given string total istitle there or not there
#Eg1:
a="You Cant See Me"
print(a.istitle())

#Eg2:
a="YES123 man"
print(a.istitle())

#Eg3:
a="SAIKUMAR1i2not good as u think"
print(a.istitle())


#write 3 programmes using isspace() function
#it will check in given string total isspace there or not there
#Eg1:
a="     "
print(a.isspace())

#Eg2:
a="YES123 \n man"
print(a.isspace())

#Eg3:
a="SAIKUMAR1i2not good as u think"
print(a.isspace())


#without using the LOWER fuction
s=input("enter any string:")
for x in s:
    s=chr(ord(x)+32)
    print(s,end="")