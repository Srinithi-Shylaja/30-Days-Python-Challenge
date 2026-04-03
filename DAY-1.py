# Day 1 - Python Basics
# Topics: Input, Arithmetic Operations, Conditionals, Swapping
# Author: Srinithi Shylaja

# -----------------------------------
# 1. Square and Cube of a Number
# -----------------------------------
num = int(input("Enter a number: "))

print("Square:", num * num)
print("Cube:", num * num * num)


# -----------------------------------
# 2. Find the Largest of Three Numbers
# -----------------------------------
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)


# -----------------------------------
# 3. Swap Two Numbers (Without Temp Variable)
# -----------------------------------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
