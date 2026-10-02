# Build a “Unit Price Calculator” using float variables for price and quantity, formatting the total to 2 decimal places.


price  = float(input("Enter price per unit: "))
quantity = float(input("Enter quantity: "))

total = price * quantity

print("Total price: {:.2f}".format(total))
