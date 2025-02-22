import random

namesString = input("Give me everybody's names, separated by a comma and a space.\n")
names = namesString.split(", ") # Split the string into a list of names

# Randomly select a name from the list and print it out
# personWhoWillPay = random.choice(names)
personWhoWillPay=names[random.randint(0, len(names) - 1)]

print(personWhoWillPay + " is going to buy the meal today!")
