# create an empty dictionary. allow 4 friends to enter their favorite language as value and use key as their names. assume that the names are unique.
d = {}
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)


# if the name of 2 friends are same ; what will happens to the program in problem6.py?
#  answer ==  change and update with second one .



# if languages of two friends are same ; what will happen to the program in problem 6? 
# answer == nothing will happen . the value can be same 
