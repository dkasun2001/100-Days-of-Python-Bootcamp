print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L :")
addPepperoni = input("Do you want pepperoni? Y or N :")
extraCheese = input("Do you want extra cheese? Y or N :")

if size == "S":
  bill = 15
  if addPepperoni == "Y":
    bill += 2
elif size == "M":
  bill = 20
  if addPepperoni == "Y":
    bill += 3
elif size == "L":
  bill = 25
  if addPepperoni == "Y":
    bill += 3
else:
  print("Wrong size")

if extraCheese == "Y":
  bill+=1

print(f"Your final bill is: {bill}")    