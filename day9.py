# day  9
# String Method

a = "!!!prince!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))  # rstrip is used to remove the trailing characters
print(a.replace("prince", "Rahul"))  # replace is used to replace the old string with the new string

print(a.split(" "))  # split is used to split the string into a list where each word is a list item

blongHeading = "introduction to python"
print(blongHeading.capitalize())  # capitalize is used to capitalize the first letter of the string

str1 = "Welcome to the console!!!"
print(len(str1))  # len is used to find the length of the string
print(len(str1.center(50)))  # center is used to center the string

str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))  # endswith is used to check if the string ends with the specified value or not and it returns true or false value and it is case sensitive .

str1 = "Welcome to the console!!!" 
print(str1.endswith("to", 4, 10)) 

str1 = "He's name is Prince. He is good boy"
print(str1.find("is"))
print(str1.find("Prince")) 

str1 = "WelcomeToTheconsole"
print(str1.isalnum())  # isalnum is used to check if the string is alphanumeric or not and it returns true or false value
str1 = "Welcome"
print(str1.isalpha()) 

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Happy Birthday"
print(str1.isprintable())  # isprintable is used to check if the string is printable or not and it returns true or false value 

str1 = "        "  # using spacebar
print(str1.isspace())

str2 = "    "  # using tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())  # istitle is used to check if the string is title or not and it returns true or false value

str2 = "To kill a Mocking bird"
print(str2.istitle()) 

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))  # startswith is used to check if the string starts with the specified value or not and it returns true or false value and it is case sensitive .

str1 = "Python is a Interpreted Language"
print(str1.swapcase())  # swapcase is used to swap the case of the string

str1 = "His name is Prince. He is good boy"
print(str1.title())  # title is used to convert the first letter of each word to uppercase and the remaining letters to lowercase.
