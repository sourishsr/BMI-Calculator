def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator App!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)
        else:
            print(f"Your BMI is: {bmi}")
            print(f"Category: {bmi_category(bmi)}")
    except ValueError:
        print("Invalid input! Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
