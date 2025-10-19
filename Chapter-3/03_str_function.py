name = "Anupam"
# name = "anupam"
print(str(name))
print(len(name))
print(name.endswith("pam"))
print(name.endswith("pa"))
print(name.startswith("Anu"))
print(name.startswith("anu")) # it is case sensitive
print(name.capitalize()) #  capitalize only starting word in whole sentence

s = "hello world"
index = s.find("world")
print(index)

s = "hello world"
replaced_string = s.replace("world" , "python")
print(replaced_string)
