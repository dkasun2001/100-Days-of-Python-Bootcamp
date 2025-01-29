print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 8
    print("Youth tickets are $8.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")  
  else:
    bill = 12
    print("Adult tickets are $12.")

  wantsPhoto = input("Do you need a photo? Y or N : ")
  if wantsPhoto =="Y":
    bill +=3
    print(f"Your tickets are ${bill}.")
  else:
    print(f"Your tickets are ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.")    