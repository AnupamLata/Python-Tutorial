def goodDay(name, ending):
    print("good day, " +name, ending)
    # print(ending)

goodDay("Harry","thank you") 
goodDay("Anupam", "thank you")
goodDay("Aniket","thanks") 

# another
def goodDay(name,ending):
    print("Good day, " +name)
    print(ending)
    return "ok"

a = goodDay("Anupam","thank you")
print(a)
