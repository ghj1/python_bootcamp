# section3.p1
# number = int(input("Which numder do you want to check? "))

# if number % 2 == 1:
#     print("This is an odd number.")
# else: 
#     print("This is a even number.")
    
# section3.p2


# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = round(height/weight**2, 0) 

# if BMI < 18.5 :
#     print(f"your BMI is {BMI}, you are underweight")
# elif BMI < 25:
#     print(f"your BMI is {BMI}, you are normal weight")
# elif BMI < 30:
#     print(f"your BMI is {BMI}, you are slightly overweight")
# elif BMI < 35:
#     print(f"your BMI is {BMI}, you are obese")
# else:
#     print(f"your BMI is {BMI}, you are clinically obese")


# section3.p3
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print("leap year")
        else: 
            print("Not leap year")
    else: 
        print("leap year")
else: 
    print("Not leap year")