height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) /(float(height)**2)

# bmi = round(bmi, 0)
bmi = int(bmi)

print("your BMI is "+str(bmi))
