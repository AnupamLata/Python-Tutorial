'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 1*2
factorial(3) = 1*2*3
factorial(4) = 1*2*3*4
factorial(5) = 1*2*3*4*5

factorial(n) = n * factorial(n-1)

'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of this number is :{factorial(n)}")
