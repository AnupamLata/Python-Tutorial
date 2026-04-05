# Write a program using functions to find greatest of three numbers.



a = 22
b = 33
c = 32

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        (c>a and c>b)
        return c
    
a = 22
b = 33
c = 32
print(f"greatest number is:{greatest(a, b, c)}")    
