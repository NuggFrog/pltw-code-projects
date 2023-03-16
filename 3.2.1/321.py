# Init vars
total = (0.00)
chickenPrice = (5.25)
beefPrice = (6.25)
tofuPrice = (5.75)
sBevPrice = (1.00)
mBevPrice = (1.75)
lBevPrice = (2.25)
sFFPrice = (1.00)
mFFPrice = (1.50)
lFFPrice = (2.00)
kPrice = (0.25)
order = []

print("Please only use the first word with the full word. For yes or no questions, answer with either Yes or No.")

# Iteration 1
# Sandwich Type Selector
sandwich = input("Would you like a Chicken Sandwich, a Beef Sandwich, a Tofu Sandwich, or nothing? ")

sandwich = sandwich.lower()

# Event Handler for sandwich
if sandwich == "chicken":
  print("You want a Chicken Sandwich for $5.25")
  total = total + chickenPrice
  order.append("Chicken Sandwich")
  
elif sandwich == "beef":
  print("You want a Beef Sandwich for $6.25")
  total = total + beefPrice
  order.append("Beef Sandwich")
  
elif sandwich == "tofu":
  print("You want a Tofu Sandwich for $5.75")
  total = total + tofuPrice
  order.append("Tofu Sandwich")

elif sandwich == "nothing":
  print("You do not want a sandwich")
  order.append("No Sandwich")
  
else:
  print("Please restart the program and input Chicken, Beef, or Tofu")
  quit()

# Iteration 2
# Drink Selector
bevQ = input("Would you like a drink? ")

bevQ = bevQ.lower()

# Drink Selection Handler
if bevQ == "yes":
    bevS = input("Would you like a Small, Medium, or a Large Drink? ")

    bevS = bevS.lower()

    # Drink Size Selector
    if bevS == "small":
        print("You want a Small Drink for $1.00")
        total = total + sBevPrice
        order.append("Small Drink")

    elif bevS == "medium":
        print("You want a Medium Drink for $1.75")
        total = total + mBevPrice
        order.append("Medium Drink")

    elif bevS == "large":
        print("You want a Large Drink for $2.25")
        total = total + lBevPrice
        order.append("Large Drink")
    else:
        print("Please restart the program and input Small, Medium, or Large")
        quit()
elif bevQ == "no":
    print("You do not want a drink")
    order.append("No Drink")
else:
    print("Please restart the program and input Yes or No")
    quit()

# Iteration 3
# French Fry Selector
ffQ = input("Would you like French Fries? ")

ffQ = ffQ.lower()

# French Fry Selection Handler
if ffQ == "yes":
    ffS = input("Would you like Small, Medium, or Large Fries? ")

    ffS = ffS.lower()

    # French Fry Size Selector
    if ffS == ("small"):
        print("You want Small Fries for $1.00")
        ffSM = input("Would you like to have your fries Mega Sized? ")

        ffSM = ffSM.lower()

        if ffSM == ("yes"):
            print("You want Mega Fries for $2.00")
            total = total + lFFPrice
            order.append("Mega Fries")
        else:
            print("You do not want Mega Fries")
            total = total + sFFPrice
            order.append("Small Fries")
    elif ffS == ("medium"):
        print("You want Medium Fries for $1.50")
        total = total + mFFPrice
        order.append("Medium Fries")
    elif ffS == ("large"):
        print("You want Large Fries for $2.00")
        total = total + lFFPrice
        order.append("Large Fries")
    else:
        print("Please restart the program and input Small, Medium, or Large")
        quit()
elif ffQ == ("no"):
    print("You do not want French Fries")
    order.append("No Fries")
else:
    print("Please restart the program and input Yes or No")
    quit()

# Iteration 4
# Ketchup Selector
kS = input("Would you like Ketchup Packets? ")

kS = kS.lower()

# Ketchup Selection Handler
if kS == ("yes"):
    # Ketchup Quantity Handler
    kQ = input("How Many Packets would you like? ")
    kQ = int(kQ)
    if kQ >= 1:
        print("You want", kQ, "Ketchup Packets for $", kQ * kPrice)
        total = total + kPrice * kQ
        order.append(f"{kQ} Ketchup Packets")
    else:
        print("You do not want Ketchup Packets")
elif kS == ("no"):
    print("You do not want Ketchup Packets")
    order.append("No Ketchup Packets")
else:
    print("Please restart the program and input Yes or No")
    quit()

# Receipt
print("This is your order:")
print(order[0])
print(order[1])
print(order[2])
print(order[3])

# Final Total
print("Your total is $", total)