# break statement example 

for i in range(5):
    if i == 3:
        break
    print(i) 

# program to find first 5 multiples of 6

i = 1
while i <= 15:
    print('6 * ',(i), '=',6 * i)
    if i >= 10:
        break
    i = i + 1

#A demo of break statement with for loop  

lst_num = [2, 4, 6, 8, 10]

for x in lst_num:
    if x == 6:
        break
    print("List item: " ,x)
print("The loop terminated at item 6") 

# Example with a string
my_str = "python"  

for char in my_str:  
    if char == 'o':  
        break  
    print(char)  

# Example with a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Found 3, breaking loop")
        break
    print(num)

# Example with a string
word = "hello"
for char in word:
    if char == 'l':
        print("Found 'l', breaking loop")
        break 
    print(char)

# Example with a tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    if coord == 20:
        print("Found 20, breaking loop")
        break
    print(coord)

# Example with a dictionary 
    
person = {"name": "John", "age": 25, "city": "New York"}
for key, value in person.items():
    if key == "age":
        print("Found 'age', breaking loop")
        break
    print(f"{key}:{value}")


#5 example on continue

for years in range(1992, 2018):

   if years % 4 == 0:
      print("Leap", years)
      continue
   
# Example with list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Skipping 3")
        continue
    print(num)

# Example with string
word = "hello"
for char in word:
    if char == 'l':
        print("Skipping 'l'")
        continue
    print(char)

# Example with tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    if coord == 20:
        print("Skipping 20")
        continue
    print(coord)

# Example with dictionary
person = {"name": "John", "age": 25, "city": "New York"}
for key, value in person.items():
    if key == "age":
        print("Skipping 'age'")
        continue
    print(f"{key}: {value}")


#5 ex on pass
   
x=10 
if x >5:
    pass 
else:
    print("x is not greater than 5")

# Example with integer
x = 42
if x > 10:
    pass
else:
    print("x is not greater than 10")

# Example with float
pi = 3.14
if pi < 4.0:
    pass
else:
    print("pi is not less than 4.0")

# Example with string
my_string = "Hello, World!"
for char in my_string:
    pass

# Example with list
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    pass

# Example with tuple
my_tuple = (10, 20, 30)
for value in my_tuple:
    
    pass

# Example with set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    pass

# Example with dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    pass

# Example with boolean
flag = True
if flag:
    pass
else:
    print("The flag is False")

# Example with NoneType
result = None
if result is None:
    pass
else:
    print("Result is not None")

#list=[10,20,0,5,7,3,2,1,0] do it with continue 
#divide with 100 

list = [10, 20, 0, 5, 7, 3, 2, 1,0]
for element in list:
  if element == 0:
    continue
print(element)