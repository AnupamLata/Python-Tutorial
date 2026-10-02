#  Write a program to inspect the memory foot print (in bytes) of different datatypes using `sys.getsizeof()`.

import sys

a = 10
b = 10.5
c = "Hello"
d = True
e = [1,2,3]
f = {1,2,3}
g = (1,2,3)
h = {"name" : "Anupam"}

print("Integer: ", sys.getsizeof(a), "bytes")
print("float: ", sys.getsizeof(b), "bytes")
print("string: ", sys.getsizeof(c), "bytes")
print("Boolean: ", sys.getsizeof(d), "bytes")
print("List: ", sys.getsizeof(e), "bytes")
print("Set: ", sys.getsizeof(f), "bytes")
print("Tuple: ", sys.getsizeof(g), "bytes")
print("Dictionary: ", sys.getsizeof(h), "bytes")
