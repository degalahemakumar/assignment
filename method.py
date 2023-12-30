# input: AMAN IS GOOD BOY
# output: aman is good boy

input_string = "AMAN IS GOOD BOY"
output_string = ""
for char in input_string:
    if 'A' <= char <= 'Z':
        output_string += chr(ord(char) + ord('a') - ord('A'))
    else:
        output_string += char

print("Input:",input_string)
print("Output:",output_string)

#input : ABCDAABBCCDEEGFGGHHHIIJK
#OUTPUT: ABCDEFGHIJK

def get_unique_characters(input_str):
    unique_chars = ""
    seen_chars = set()

    for char in input_str:
        if char not in seen_chars:
            unique_chars += char
            seen_chars.add(char)

    return unique_chars

input_string = "ABCDAABBCCDEEGFGGHHHIIJK"
output_string = get_unique_characters(input_string)

print("Input:",input_string)
print("Output:",output_string)

#isalnum()
#Example 1
string1 = "hemakumar"
result1 = string1.isalnum()
print(f"Example 1: '{string1}' is alphanumeric?{result1}")

# Example 2
string2 = "kumar1998"
result2 = string2.isalnum()
print(f"Example 2: '{string2}' is alphanumeric?{result2}")

# Example 3
string3 = "12345"
result3 = string3.isalnum()
print(f"Example 3: '{string3}' is alphanumeric?{result3}")

# Example 4
string4 = "Special@Chars"
result4 = string4.isalnum()
print(f"Example 4: '{string4}' is alphanumeric?{result4}")

# Example 5
string5 = "Spaces Are Not Allowed"
result5 = string5.isalnum()
print(f"Example 5: '{string5}' is alphanumeric?{result5}")

#isalpha()

# Example 1
string1 = "hi good morning"
result1 = string1.isalpha()
print(f"Example 1: '{string1}' is alphabetic? {result1}")

# Example 2
string2 = "kumar hema"
result2 = string2.isalpha()
print(f"Example 2: '{string2}' is alphabetic? {result2}")

# Example 3
string3 = "9581701052"
result3 = string3.isalpha()
print(f"Example 3: '{string3}' is alphabetic? {result3}")

# Example 4
string4 = "SpecialChars"
result4 = string4.isalpha()
print(f"Example 4: '{string4}' is alphabetic? {result4}")

# Example 5
string5 = "Spaces Are Not Allowed"
result5 = string5.isalpha()
print(f"Example 5:'{string5}' is alphabetic?{result5}")

#isdigit()

# Example 1
string1 = "12345"
result1 = string1.isdigit()
print(f"Example 1: '{string1}' is composed of digits? {result1}")

# Example 2
string2 = "gopal3"
result2 = string2.isdigit()
print(f"Example 2: '{string2}' is composed of digits? {result2}")

# Example 3
string3 = "42.0,6.7,8,9.8"
result3 = string3.isdigit()
print(f"Example 3: '{string3}' is composed of digits? {result3}")

# Example 4
string4 = "SpecialChars"
result4 = string4.isdigit()
print(f"Example 4: '{string4}' is composed of digits? {result4}")

# Example 5
string5 = "123 456 56 78 "
result5 = string5.isdigit()
print(f"Example 5: '{string5}' is composed of digits? {result5}")

#islower()

# Example 1
string1 = "ram is good boy"
result1 = string1.islower()
print(f"Example 1: '{string1}' is in lowercase? {result1}")

# Example 2
string2 = "prasad"
result2 = string2.islower()
print(f"Example 2: '{string2}' is in lowercase? {result2}")

# Example 3
string3 = "lowercase123"
result3 = string3.islower()
print(f"Example 3: '{string3}' is in lowercase? {result3}")

# Example 4
string4 = "MixedCase"
result4 = string4.islower()
print(f"Example 4: '{string4}' is in lowercase? {result4}")

# Example 5
string5 = "   alllowercase   "
result5 = string5.islower()
print(f"Example 5: '{string5}' is in lowercase? {result5}")

#isupper()

# Example 1
string1 = "SAI IS A PLAYING CRICKET"
result1 = string1.isupper()
print(f"Example 1: '{string1}' is in uppercase? {result1}")

# Example 2
string2 = "hema kumar"
result2 = string2.isupper()
print(f"Example 2: '{string2}' is in uppercase? {result2}")

# Example 3
string3 = "UPPERCASE123"
result3 = string3.isupper()
print(f"Example 3: '{string3}' is in uppercase? {result3}")

# Example 4
string4 = "MixedCase"
result4 = string4.isupper()
print(f"Example 4: '{string4}' is in uppercase? {result4}")

# Example 5
string5 = "   ALLUPPERCASE   "
result5 = string5.isupper()
print(f"Example 5: '{string5}' is in uppercase? {result5}")


#istittle()

# Example 1
string1 = "Title Case Example"
result1 = string1.istitle()
print(f"Example 1: '{string1}' is in title case? {result1}")

# Example 2
string2 = "Not Title Case"
result2 = string2.istitle()
print(f"Example 2: '{string2}' is in title case? {result2}")

# Example 3
string3 = "123 Title Case"
result3 = string3.istitle()
print(f"Example 3: '{string3}' is in title case? {result3}")

# Example 4
string4 = "maruthi 123"
result4 = string4.istitle()
print(f"Example 4: '{string4}' is in title case? {result4}")

# Example 5
string5 = "   Title Case   "
result5 = string5.istitle()
print(f"Example 5: '{string5}' is in title case? {result5}")


#isspace() 

# Example 1
string1 = "    "
result1 = string1.isspace()
print(f"Example 1: '{string1}' consists of whitespace characters? {result1}") 

# Example 2
string2 = "Not just spaces"
result2 = string2.isspace()
print(f"Example 2: '{string2}' consists of whitespace characters? {result2}")

# Example 3 
string3 = "\t\t\t"
result3 = string3.isspace()
print(f"Example 3: '{string3}' consists of whitespace characters? {result3}")

# Example 4
string4 = "\n\n\n"
result4 = string4.isspace()
print(f"Example 4: '{string4}' consists of whitespace characters? {result4}")

# Example 5
string5 = "   Spaces with Line Breaks\n\n\n"
result5 = string5.isspace()
print(f"Example 5: '{string5}' consists of whitespace characters?{result5}")  

# upper()

# Example 1
original_string = "hello, goodmorning"
uppercase_string = original_string.upper()
print(uppercase_string)


# Example 2
name = "hema kumar"
uppercase_name = name.upper()
print(uppercase_name)


# Example 3
sentence = "python is fun."
uppercase_sentence = sentence.upper()
print(uppercase_sentence)


# Example 4
mixed_case = "ThIs iS a MiXeD CaSe sTrInG."
uppercase_mixed_case = mixed_case.upper()
print(uppercase_mixed_case)


# Example 5
text_with_numbers = "hello123"
uppercase_text_with_numbers = text_with_numbers.upper()
print(uppercase_text_with_numbers)



# lower()

# Example 1
original_string = "HELLO, MY FRIEND!"
lowercase_string = original_string.lower()
print(lowercase_string)

# Example 2
name = "SRINUVASULU"
lowercase_name = name.lower()
print(lowercase_name)


# Example 3
sentence = "PYTHON IS FUN."
lowercase_sentence = sentence.lower()
print(lowercase_sentence)


# Example 4
mixed_case = "ThIs Is A MiXeD CaSe StRiNg."
lowercase_mixed_case = mixed_case.lower()
print(lowercase_mixed_case)


# Example 5
text_with_numbers = "Hello123"
lowercase_text_with_numbers = text_with_numbers.lower()
print(lowercase_text_with_numbers)


# swapcase()

# Example 1
original_string = "Hello, hema"
swapped_string = original_string.swapcase()
print(swapped_string)


# Example 2
name = "kumar"
swapped_name = name.swapcase()
print(swapped_name)


# Example 3
sentence = "Python is Fun."
swapped_sentence = sentence.swapcase()
print(swapped_sentence)


# Example 4
mixed_case = "ThIs Is A MiXeD CaSe StRiNg."
swapped_mixed_case = mixed_case.swapcase()
print(swapped_mixed_case)


# Example 5
text_with_numbers = "Hello123"
swapped_text_with_numbers = text_with_numbers.swapcase()
print(swapped_text_with_numbers)

# tittle()

# Example 1
original_string = "hello,prasad!"
title_string = original_string.title()
print(title_string)


# Example 2
name = "srinu,gopal,raju,raju"
title_name = name.title()
print(title_name)


# Example 3
sentence = "python is great lerning langauge"
title_sentence = sentence.title()
print(title_sentence)


# Example 4
mixed_case = "ThIs iS a MiXeD CaSe sTrInG"
title_mixed_case = mixed_case.title()
print(title_mixed_case)


# Example 5
text_with_numbers = "mike testiing friends 123"
title_text_with_numbers = text_with_numbers.title()
print(title_text_with_numbers)

# capitalize()

# Example 1

original_string = "hello, hema,Maruthi,Gopal"
capitalized_string = original_string.capitalize()
print(capitalized_string)


# Example 2
name = "hema kumar"
capitalized_name = name.capitalize()
print(capitalized_name)


# Example 3
sentence = "raju is a palaying cricket "
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence)


# Example 4
mixed_case = "ThIs iS a MiXeD CaSe sTrInG."
capitalized_mixed_case = mixed_case.capitalize()
print(capitalized_mixed_case)


# Example 5
text_with_numbers = "hello123 good morning"
capitalized_text_with_numbers = text_with_numbers.capitalize()
print(capitalized_text_with_numbers)