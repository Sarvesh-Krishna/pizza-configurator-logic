print("------------Welcome------------")
print("----------Pizza World----------")
size=input("Size of pizza 'p' for personal & 'f' for family: ")
if size=="p":
    size="personal"
else:
    size="family"
sauce=input("which sauce would you like to add on 'm' for marinara & 'g' for garlic cream: ")
if sauce=="m":
    sauce="marinara"
else:
    sauce="garlic cream"
cheese=input("would you like to have cheese (y/n): ")
if cheese=="y":
    cheese1=input("whether its regular or extra (r/e): ")
    if cheese1=="r":
        cheese="regular"
    else:
        cheese="extra"
else:
    cheese="no"
topping1=input("would you like to add onion (y/n): ")
if topping1=="y":
    topping1="onion"
else:
    topping1="no onion"

topping2=input("would you like to add olive (y/n): ")
if topping2=="y":
    topping2="olive"
else:
    topping2="no olive"

topping3=input("would you like to add mushroom (y/n): ")
if topping3=="y":
    topping3="mushroom"
else:
    topping3="no mushroom"

topping4=input("would you like to add paneer (y/n): ")
if topping4=="y":
    topping4="paneer"
else:
    topping4="no paneer"
print(f"Your order is: {size} pizza with {sauce} sauce with {cheese} cheese and toppings are: {topping1}, {topping2}, {topping3} & {topping4}")
print("Thank you for your order!!!")
    
        
