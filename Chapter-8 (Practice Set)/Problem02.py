''' 
Write a python program using function to convert celisius to fahrenteit.
formula = (c/5 = f-32/9) 
'''
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(f_to_c(f), 2)} degree C")    
