fris = 0
bevs = 0
mega = "n"
sandt = ""
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
bev = "n"
fri = "n"
kat = 'y'
kats = 0
print("To skip the question at any time, or back out of choosing, simply answer \"q\" ")
sand = input("Do you want a sandwich? Answer with (y/n)").upper()
while sand != "Y" and sand != "N" and sand != "Q":
    if sand == "Q":
        break
    print("That is not a valid option")
if sand == "Y":
    sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75 ").lower()
    while sandt != "chicken" and sandt != "beef" and sandt != "tofu" and sandt != "q":
        if sandt == "q":
            sand = "N"
            break
        print("That is not a valid option.")
        sandt = input("What kind of sandwich do you want? \n Chicken $5.25 \n Beef $6.25 \n Tofu $5.75 ").lower()
    if sandt == "chicken":
        c1 = 5.25
    elif sandt == "beef":
        c1 = 6.25
    elif sandt == "tofu":
        c1 = 5.75

bev = input("Would you like a beverage? Answer with (y/n)").upper()
while bev != "Y" and bev != "N" and bev != "Q":
    if bev == "Q":
        break
    print("That is not a valid option.")
    bev = input("Would you like a beverage? Answer with (y/n)").upper()
if bev == "Y":
    bevs = input("What size would you like of drink? \n Small $1.00 \n Medium $1.75 \n Large $2.25").upper()
    while bevs != "SMALL" and bevs != "MEDIUM" and bevs != "LARGE" and bevs != "Q":
        if bevs == "Q":
            bev = "N"
            break
        print("That is not a valid option.")
        bevs = input("What size would you like of drink? \n Small $1.00 \n Medium $1.75 \n Large $2.25").upper()
    if bevs == "SMALL":
        c2 = 1.00
    elif bevs == "MEDIUM":
        c2 = 1.75
    elif bevs == "LARGE":
        c2 = 2.25

fri = input("Would you like fries? Answer with (y/n)").lower()
while fri != "y" and fri != "n" and fri != "q":
    if fri == "q":
        break
    print("That is not a valid option.")
    fri = input("Would you like fries? Answer with (y/n)").lower()
if fri == "y":
    fris = input("What size would you like of fries? \n Small $1.00 \n Medium $1.50 \n Large $2.00").lower()
    while fris != "small" and fris != "medium" and fris != "large" and fris != q:
        if fris == "q":
            fri = "n"
            break
        print("That is not a valid option.")
        fris = input("What size would you like of fries? \n Small $1.00 \n Medium $1.50 \n Large $2.00").lower()
    if fris == "small":
        c3 = 1.00
        mega = input("Would you like to mega-size your fries? Answer with (y/n)").lower()
        while mega != "y" and mega != "n" and mega != "q":
            if mega == "q":
                break
            print("That is not a valid option.")
            mega = input("Would you like to mega-size your fries? Answer with (y/n)").lower()
        if mega == "y":
            c3 = 2.00
            fris = "MEGA"
    elif fris == "medium":
        c3 = 1.50
    elif fris == "large":
        c3 = 2.00

kat = input("Do you want ketchup? Answer with (y/n)").lower()
while kat != "y" and kat != "n" and kat != "q":
    if kat == "q":
        break
    print("That is not a valid option.")
    kat = input("Do you want ketchup? Answer with (y/n)").lower()
if kat == "y":
    kats = int(input("How many ketchup packets do you want? \n 1 Ketchup is $0.25"))
    while kats < 1:
        if kats == "q":
            kat = "n"
            break 
        print("That is not a valid option.")
        kats = int(input("How many ketchup packets do you want? \n 1 Ketchup is $0.25"))
    c4 = .25 * kats

if bev == "Y" and fri == "y" and kat == "y":
    c5 = -1 

if sand == "Y":
    print("You chose {} for your sandwich".format(sandt))
if bev == "Y":
    print("You chose the {} size for your drink.".format(bevs))
if fri == "y":
    print("You chose the {} size for your fries.".format(fris))
if kat == "y":
    print("You got {} ketchup packets".format(kats))
scost = c1 + c2 + c3 + c4 + c5
tcost = (c1 + c2 + c3 + c4 + c5) * 1.08
print("The subtotal  is ${:.2f}, the total is {:.2f}".format(scost, tcost))











