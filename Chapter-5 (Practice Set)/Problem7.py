#  can you change the values inside a list which is contained in set S ?


s = {8, 7, 12, 'Harry', [1, 2]}
# answer ==  no, you cannot change the  values inside a list contained in a set in python .in fact , you cannot even have a list as an element in a set because sets in python require all their element to be immutable and hashable. lists are mutable and not hashable , so they cannot be added to a set.
#  if you try to create a set with a list as one of its elements, python will raise a 'TypeError'. here is an example of what happens:
