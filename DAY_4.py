# Day 4 - Logic Building Problems
# Topics: Numbers, Patterns, Loops
# Author: Srinithi Shylaja

# -----------------------------------
# 1. Reverse a Number
# -----------------------------------
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)


# -----------------------------------
# 2. Check Palindrome Number
# -----------------------------------
num = int(input("\nEnter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")


# -----------------------------------
# 3. Count Digits in a Number
# -----------------------------------
num = int(input("\nEnter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)


# -----------------------------------
# 4. Sum of Digits
# -----------------------------------
num = int(input("\nEnter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)


# -----------------------------------
# 5. Armstrong Number
# -----------------------------------
num = int(input("\nEnter a number: "))
temp = num
power = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# -----------------------------------
# 6. Multiplication Table
# -----------------------------------
num = int(input("\nEnter a number: "))

print("Multiplication Table:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -----------------------------------
# 7. Pattern Printing
# -----------------------------------
print("\nPattern 1:")
for i in range(1, 5):
    print("*" * i)

print("\nPattern 2:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# -----------------------------------
# 8. Largest Digit in a Number
# -----------------------------------
num = int(input("\nEnter a number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("Largest digit:", largest)


# -----------------------------------
# 9. Prime Numbers in a Range
# -----------------------------------
start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
