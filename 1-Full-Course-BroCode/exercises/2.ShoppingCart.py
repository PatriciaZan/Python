
item = input("What item would you like to buy?: ")
price = float(input("What is teh price?: "))
quantity = int(input("How many items would you like?: "))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"The total price is R${total}")