phrase = "Remove spaces from this phrase."
no_spaces = phrase.replace(" ", "")
print(no_spaces) 

#R find() 5 Example

# Example 1
new = "Hello, World!"
index = new.rfind("o")
print("Example 1:",index)  

# Example 2
text ="Python is powerful and easy to learn."
index=text.rfind("easy")
print("Example 2:",index)  

# Example 3
member ="Programming is fun.Python is also fun."
index =member.rfind("fun")
print("Example 3:",index)  

# Example 4
line ="Python is awesome.Python is versatile."
index =line.rfind("Python",7,20)
print("Example 4:", index)  

# Example 5
product ="Python programming is fun.Python is versatile."
index =product.rfind("Python",1,40)
print("Example 5:", index) 

# find() 5 Example

# Example 1
string = "Hello, World!"
index =string.find("o")
print("Example 1:",index)  

# Example 2
word_text ="raju is a playing cricket"
index =word_text.find("playing")
print("Example 2:",index)  

# Example 3
name ="chiru is a good boy.chiru is a good dancer."
index = name.find("chiru")
print("Example 3:",index) 

# Example 4
hero ="Python is awesome. Python is versatile."
index =hero.find("Python", 10)
print("Example 4:",index)  

# Example 5
text ="Python programming is fun. Python is versatile."
index =text.find("Python", 10, 30)
print("Example 5:",index)  

# index 5 example

# Example 1
text ="Hello, World!"
index =text.index("World")
print("Example 1:", index)  

# Example 2
text ="Python is powerful and easy to learn."
index =text.index("easy")
print("Example 2:", index)  

# Example 3
text ="Programming is fun."
try:
    index =text.index("Python")
    print("Example 3:",index)
except ValueError:
    print("Example 3:Substring not found")

# Example 4
text ="Python is awesome. Python is versatile."
index =text.index("Python", 10)
print("Example 4:", index)  

# Example 5
text = "Python programming"
try:
    index = text.index("gram", 7, 15)
    print("Example 5:", index)
except ValueError:
    print("Example 5: Substringnotfound")

#r index 5 example
    
# Example 1
text = "Hello,prasad!"
index = text.find("World")
print("Example 1:",index)  

# Example 2
text ="Python is powerful and easy to learn."
index =text.find("easy")
print("Example 2:",index)  

# Example 3
text ="Programming is fun."
index =text.find("Python")
print("Example 3:",index)  

# Example 4
text ="Python is awesome. Python is versatile."
index =text.find("Python",10)
print("Example 4:",index)  

# Example 5
text ="Python programming"
index=text.find("gram",7,15)
print("Example 5:",index)