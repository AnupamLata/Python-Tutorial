#  Write a program that demonstrates mutable vs. immutable data types using a list and a tuple, showing identical operations on each.

# Mutable data type -List
my_list = [10, 20, 30]

print("Orignal List: ", my_list)

my_list[0] =  100

print("Modified List: ", my_list)

# Immutable data type - Tuple
my_tuple = (10, 20, 30)

print("Orignal Tuple: ", my_tuple)

try:
    my_tuple[0] = 100
except TypeError:

    print("Tuple cannot be modified.")
