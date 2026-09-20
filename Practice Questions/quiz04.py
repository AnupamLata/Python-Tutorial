# Create a script that takes a user's name and job role as input and prints a formatted,multi-line welcome banner.

name = input("Enter your name :")
job_role = input("Enter your job role: ")

print("\n" + "=" * 35)
print("        WELCOME")

print("=" *35)

print(f"Hello, {name}!")
print(f"Role : {job_role}")

print("We are happy to have you with us")

print("=" * 35)
