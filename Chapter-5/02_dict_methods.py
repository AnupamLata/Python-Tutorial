marks = {
    "Harry" : 100,
    "Aniket" : 56,
    "Anupam"  : 34,
    0 : "Harry"
}
# print(marks.items())
# print(marks.keys())
print(marks.popitem())
print(marks.values())

marks.update({"Harry" : 99})
# or doing this for adding something
marks.update({"Harry" : 99, "Anushka" : 87})

print(marks)

print(marks.get("Aniket")) 
print(marks["Aniket"])

# for more dict methods use chatgpt




# for knowledge
print(marks.get("Aniket2")) # when print ans is none
print(marks["Aniket2"]) # when print ans is error

