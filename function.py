def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
user_input = int(input("Enter a number: "))
result = is_even_or_odd(user_input)
print(f"The given number is {result}.") 

#take a nd b and do add,mul,div,sub  

# Input two numbers from the user
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

def perform_operations(a, b):
    # Addition
    addition_result = a + b
    print(f"Addition result: {addition_result}")

    # Subtraction
    subtraction_result = a - b
    print(f"Subtraction result: {subtraction_result}")

    # Multiplication
    multiplication_result = a * b
    print(f"Multiplication result: {multiplication_result}")

    # Division (check for division by zero)
    if b != 0:
        division_result = a / b
        print(f"Division result: {division_result}")
    else:
        print("Cannot divide by zero.")



# Call the function to perform operations
perform_operations(a, b) 

# Factorial Calculation:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result) 

#String Reversal

def reverse_string(s):
    return s[::-1]

result = reverse_string("hello")
print(result) 

#List Sorting: 

def sort_list(lst):
    return sorted(lst)

result = sort_list([3, 1, 4, 1, 5, 9, 2])
print(result) 

#Maximum of Three Numbers: 

def max_of_three(a, b, c):
    return max(a, b, c)

result = max_of_three(5, 12, 8)
print(result) 

#Dictionary Key Checker: 

def has_key(d, key):
    return key in d

sample_dict = {'a': 1, 'b': 2, 'c': 3}
result = has_key(sample_dict, 'b')
print(result) 

#List Squaring:

def square_list(lst):
    return [x ** 2 for x in lst]

result = square_list([1, 2, 3, 4, 5])
print(result) 

#File Reader: 

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

content = read_file('example.txt')
print(content) 

#Simple Calculator: 

def calculator(a, b, operation='+'):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "Invalid operation"

result = calculator(10, 5, '-')
print(result) 

#Palindrome Checker: 

def is_palindrome(s):
    cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_str == cleaned_str[::-1]

result = is_palindrome("A man, a plan, a canal, Panama!")
print(result)  

#List Intersection:

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

result = intersection([1, 2, 3, 4], [3, 4, 5, 6])
print(result) 

#Fibonacci Sequence Generator 

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

result = generate_fibonacci(8)
print(result) 

#Title Case Converter: 

def to_title_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

result = to_title_case("hello world, how are you?")
print(result) 


#Prime Number Checker: 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

result = is_prime(17) 
print(result)