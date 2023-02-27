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
sBool = False
sCBool = False
sBBool = False
sTBool = False
dBool = False
dSBool = False
dMBool = False
dLBool = False
fBool = False
fSBool = False
fMBool = False
fLBool = False
fMeBool = False
kBool = False

print("Please only use the first word with the full word. For yes or no questions, answer with either Yes or No.")

# Iteration 1
# Sandwich Type Selector
sandwich = input("Would you like a Chicken Sandwich, a Beef Sandwich, or a Tofu Sandwich?")

sandwich = sandwich.lower()

# Event Handler for sandwich
if sandwich == "chicken":
  print("You want a Chicken Sandwich for $5.25")
  total = total + chickenPrice
  sBool = True
  sCBool = True
elif sandwich == "beef":
  print("You want a Beef Sandwich for $6.25")
  total = total + beefPrice
  sBool = True
  sBBool = True
elif sandwich == "tofu":
  print("You want a Tofu Sandwich for $5.75")
  total = total + tofuPrice
  sBool = True
  sTBool = True
else:
  print("Please restart the program and input Chicken, Beef, or Tofu")
  quit()

# Iteration 2
# Drink Selector
bevQ = input("Would you like a drink?")

bevQ = bevQ.lower()

# Drink Selection Handler
if bevQ == "yes":
    dBool = True
    bevS = input("Would you like a Small, Medium, or a Large Drink?")

    bevS = bevS.lower()

    # Drink Size Selector
    if bevS == "small":
        print("You want a Small Drink for $1.00")
        total = total + sBevPrice
        dSBool = True
    elif bevS == "medium":
        print("You want a Medium Drink for $1.75")
        total = total + mBevPrice
        dMBool = True
    elif bevS == "large":
        print("You want a Large Drink for $2.25")
        total = total + lBevPrice
        dLBool = True
    else:
        print("Please restart the program and input Small, Medium, or Large")
        quit()
elif bevQ == "no":
    print("You do not want a drink")
else:
    print("Please restart the program and input Yes or No")

# Iteration 3
# French Fry Selector
ffQ = input("Would you like French Fries?")

ffQ = ffQ.lower()

# French Fry Selection Handler
if ffQ == "yes":
    fBool = True
    ffS = input("Would you like Small, Medium, or Large Fries?")

    ffS = ffS.lower()

    # French Fry Size Selector
    if ffS == ("small"):
        fSBool = True
        print("You want Small Fries for $1.00")
        ffSM = input("Would you like to have your fries Mega Sized?")

        ffSM = ffSM.lower()


        if ffSM == ("yes"):
            print("You want Mega Fries for $2.00")
            total = total + lFFPrice
            fMeBool = True
            fSBool = False
        else:
            print("You do not want Mega Fries")
            total = total + sFFPrice
    elif ffS == ("medium"):
        print("You want Medium Fries for $1.50")
        total = total + mFFPrice
        fMBool = True
    elif ffS == ("large"):
        print("You want Large Fries for $2.00")
        total = total + lFFPrice
        fLBool = True
    else:
        print("Please restart the program and input Small, Medium, or Large")
        quit()
elif ffQ == ("no"):
    print("You do not want French Fries")
else:
    print("Please restart the program and input Yes or No")
    quit()

# Iteration 4
# Ketchup Selector
kS = input("Would you like Ketchup Packets?")

kS = kS.lower()

# Ketchup Selection Handler
if kS == ("yes"):
    kBool = True
    # Ketchup Quantity Handler
    kQ = input("How Many Packets would you like?")
    kQ = int(kQ)
    if kQ >= 1:
        print("You want", kQ, "Ketchup Packets for $", kQ * kPrice)
        total = total + kPrice * kQ
    else:
        print("You do not want Ketchup Packets")
elif kS == ("no"):
    print("You do not want Ketchup Packets")
else:
    print("Please restart the program and input Yes or No")
    quit()

# Combo Discount Handler
if sBool == True and dBool == True and fBool == True:
    print("You get $1.00 for the Combo Discount!")
    total = total - 1.00

# Receipt
print("Your order is:")
if sCBool == True:
    print("1 Chicken Sandwich")
elif sBBool == True:
    print("1 Beef Sandwich")
elif sTBool == True:
    print("1 Tofu Sandwich")

if dBool == True:
    if dSBool == True:
        print("1 Small Drink")
    elif dMBool == True:
        print("1 Medium Drink")
    elif dLBool == True:
        print("1 Large Drink")

if fBool == True:
    if fSBool == True:
        print("1 Small Fry")
    elif fMBool == True:
        print("1 Medium Fry")
    elif fLBool == True:
        print("1 Large Fry")
    elif fMeBool == True:
        print("1 Mega Fry")

if kBool == True:
    if kQ == 1:
        print("1 Ketchup Packet")
    if kQ > 1:
        print("{0} Ketchup Packets".format(kQ))

# Final Total
print("Your total is $", total)
