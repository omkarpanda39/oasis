def bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi_value = bmi(weight, height)

print(f"Your BMI is: {bmi_value:.2f}")

if bmi_value < 18.5:
    print("You are underweight")
elif 18.5 <= bmi_value < 24.9:
    print("You are a healthy weight")
elif 24.9 <= bmi_value < 29.9:
    print("You are overweight")
else:
    print("You are obese")
