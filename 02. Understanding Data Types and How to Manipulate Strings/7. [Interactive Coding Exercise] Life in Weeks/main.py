age = input("What is your current age? ")

age = int(age)

years = 90 - age 
days = years*365
weeks = years*52
months = years*12

print(f"You have {days} days, {weeks} weeks and {months} months left")