

age = int(input("What is your age?: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be +18 to sign up!")


# BOOLEAN
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")