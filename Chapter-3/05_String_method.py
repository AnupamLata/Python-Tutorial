# using string methods

# .upper()
text = "hello world"
print(text.upper())

# .lower()
print(text.lower())

# .title()

print("welcome to python".title())

# .strip()
text2 = "  hello  "
print(text2.strip())

# .replace(old,new)
text3 = "i like java"
print(text3.replace("java", "python"))

# .split(separator)
text4 =  "apple, banana, cherry"
print(text4.split(","))

# .jion(iterable)
words = ["I", "love", "python"]
print(" ".join(words))

# .find(substring)
text5 = "Python Programming"
print(text5.find("Pro"))

# .count(substring)
print("banana".count("a"))
print("banana".count("v"))

