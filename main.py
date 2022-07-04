print("Welcome, Here you can calculate your BMI")
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in kg: "))
Height = Height / 100
Hght = Height * Height
BMI = Weight / Hght
print("Your BMI is: ", BMI)
if BMI > 0:
    if BMI <= 16:
        print("You are severally underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 24.90:
        print("You are healthy")
    elif BMI <= 29.90:
        print("You are overweight")
    else:
        print("You are severally overweight")

else:
    print("Please enter valid values")

