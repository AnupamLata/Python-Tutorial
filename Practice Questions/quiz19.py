# Write a program to check whether a string represents a valid number and convert it safely without raising unhandled errors.

s = input("Enter a number: ")

try:
    num = float(s)
    print("Valid number:", num)
except ValueError:
    print("Invalid number!")
