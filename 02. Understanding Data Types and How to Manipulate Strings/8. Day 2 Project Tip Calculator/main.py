print("Welcome to the tip calculator.")
totalBill = input("What was the total bill? $")
totalBill = float(totalBill)

tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip = float(tip)/100

fullPayment = totalBill + (totalBill*tip)

peoples = input("How many people to split the bill? ")
peoples = int(peoples)

# singlePayment = round(fullPayment/peoples,2)
singlePayment = "{:.2f}".format(fullPayment/peoples)

print(f"Each person should pay: ${singlePayment}")