# Implement a function that checks if a given word is a palindrome (reads the same forwards and backwards).


# def is_palindrome(word):
#     word = word.lower().replace(" ", "")
#     return word == word[::-1]

# print(is_palindrome("Race Car"))

# or

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))



