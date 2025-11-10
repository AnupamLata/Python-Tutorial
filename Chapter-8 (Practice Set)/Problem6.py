# Write a python function which converts inches to cms. 2.54

def inches_to_cms(inch):
     return inch *2.54

n = int(input("Enter value in inches: "))

print(f"the corresponding value in cms is {inches_to_cms(n)}")
