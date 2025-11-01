# set Methods

# .add(x)  Add element
nums ={1, 2, 3}
nums.add(4)
print(nums)

# .update(iterable)
nums = {1, 2, 3}
nums.update([0.3, 6])
print(nums)

# .remove(x)
nums ={1, 2, 3}
nums.remove(3)
print(nums)

# .clear()
nums = {1, 2, 3}
nums.clear()
print(nums)

# .discard(x)
nums = {1, 2, 3}
nums.discard(10)
print(nums)

# .union(set2)
# return union of sets.
a = {1,2,3}
b = {6,4,5}
print(a.union(b))

# .intersection(set2)
# common elements.
c = {2, 3, 4}
d = {4, 3, 6}
print(c.intersection(d))

# .difference(set2)
# element in a but not in b.
e = {4, 5, 2, 6}
f = {6, 5, 7, 8}
print(e.difference(f))
print(f.difference(e))
