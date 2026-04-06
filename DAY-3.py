# Day 3 - Python Loops
# Topics: For Loop, While Loop, Number Operations
# Author: Srinithi Shylaja

# -----------------------------------
# 1. Print Numbers from 1 to 50
# -----------------------------------
for i in range(1, 51):
    print(i)


# -----------------------------------
# 2. Print Even Numbers from 1 to 50
# -----------------------------------
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# -----------------------------------
# 3. Sum of First N Numbers
# -----------------------------------
n = int(input("\nEnter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# -----------------------------------
# 4. Factorial of a Number
# -----------------------------------
n = int(input("\nEnter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


# -----------------------------------
# 5. Multiplication Table
# -----------------------------------
num = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -----------------------------------
# 6. Reverse a Number
# -----------------------------------
n = int(input("\nEnter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number =", rev)


# -----------------------------------
# 7. Count Digits in a Number
# -----------------------------------
n = int(input("\nEnter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits =", count)


# -----------------------------------
# 8. Sum of Digits
# -----------------------------------
n = int(input("\nEnter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits =", total)
