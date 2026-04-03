# Day 2 - Conditionals in Python
# Topics: If-Else, Leap Year, Grading System
# Author: Srinithi Shylaja

# -----------------------------------
# 1. Check Positive, Negative or Zero
# -----------------------------------
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# -----------------------------------
# 2. Leap Year Checker
# -----------------------------------
year = int(input("\nEnter a year: "))

if 1000 <= year <= 9999:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Year", year, "is a leap year.")
    else:
        print("Year", year, "is not a leap year.")
else:
    print("Enter a valid 4-digit year")


# -----------------------------------
# 3. Grade Calculator with Validation
# -----------------------------------
marks = int(input("\nEnter marks out of 100: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
else:
    print("Your grade is:")
    
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")
    
    
