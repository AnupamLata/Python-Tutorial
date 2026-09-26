# Create a script to convert user-entered strings into int, float,and complex numbers, handling invalid input gracefully.


value = input("Enter a number: ")

try:
    print("Interger: ", int(value))
except ValueError:
    print("Invalid input for integer.")    

try:
    print("Float: ", float(value))
except ValueError:
    print("Invalid input for float.")

try:
    print("Complex: ", complex(value))
except ValueError:
    print("Invalid input for complex number.")               

