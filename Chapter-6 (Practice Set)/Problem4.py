# Write a program to find whether a given username contain less than 10 characters no not.

username = (input("Enter the username: "))

if (len(username)<10):
    print("your username contains less than 10 characters")

else:
    print("your username contains more than or equal to 10 characters")    

    #  if we only use (username<10)
    # you cannot directly compare a string with an integer - that's why you see the typeError
    # so instead, we use
    # len(username)
    # this gives an integer . then comparing it with 10 works fine
