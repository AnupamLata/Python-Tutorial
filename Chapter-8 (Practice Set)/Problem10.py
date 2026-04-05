# Create a function that takes a list of numbers and returns the sum of all even numbers in the list.

def sum_even_num(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num

    return total

print(sum_even_num([1,2,3,4,5,6]))        
