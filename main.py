# Task 1: Variables & Data Types
# Declare variables of different data types
string_var = "Hello World"
# A string is a sequence of characters used to store text.
int_var = 16
# An integer is a whole number without a decimal point.
float_var = 5.19
# A float is a number with a decimal point
bool_var = True
# A boolean represents either True or False 
list_var = [2, 4, 6, 8]
# A list is an ordered, mutable collection of objects, written in square brackets.

# Print each variable along with its data type using the type() function
print(f"String: {string_var}, Type: {type(string_var)}")
print(f"Integer: {int_var}, Type: {type(int_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"Boolean: {bool_var}, Type: {type(bool_var)}")
print(f"List: {list_var}, Type: {type(list_var)}")

# Task 2: User Input & Conditional Statements
# Ask the user to input their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
# Task 3: Loops
# Write a for loop that prints numbers from 1 to 10
print("\nFor loop: Number from 1 to 10")
for x in range(1, 11):
    print(x)
#Write a while loop tht prints even numbers between 1 and 20
print("\nWhile loop: Even numbers between 1 and 20")
x = 2
while x <= 20:
    print(x)
    x += 2

# Task 4: Mini Challenge
# Create a list of 5 fruits
fruits = ["apple", "pawpaw", "mango", "banana", "pineapple", "orange"]

#Use a loop to print each fruit in uppercase letters
print("\nMini Challenge: Fruits in uppercase letters (excluding banana) ")
for fruit in fruits:
    if fruit =="banana":
        continue #"banana" will be skipped
    print(fruit.upper())