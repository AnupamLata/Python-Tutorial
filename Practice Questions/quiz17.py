# Write a program demonstrating variable scope (global vs. local) by modifying a counter inside and outside a function.

counter = 0

print("Before function:", counter)

def increase_counter():
    global counter
    counter = counter + 1
    print("Inside function:", counter)

increase_counter()

counter = counter + 1

print("After function:", counter)
