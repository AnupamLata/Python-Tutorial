# Build a script that demonstrates the correct use of comments, docstrings, and fstring formatting in a single file.


"""This program demonstrates comments and f-string."""

# take input from user

name = input("Enter your name: ")

# use f-string formatting

print(f"welcome, {name}")



# or
"""
This program demonstrates comments, docstrings and f-strings.
"""
# take a user input
name = input("Enter your name: ")
role = input("Enter your role: ")

def welcome (name, role):
    """Display a welcome message."""

    # Use f-string for formatting

    return f"Welcome , {name}! Your role is {role}."


print(welcome(name, role))

    
