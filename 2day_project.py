print("Welcome to the tip calculation")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10,12 or 15?"))
split_bill = int(input("How many people to split the bill? "))

if tip == 10:
    re = round(float(total_bill * 1.10)/split_bill,2)
elif tip == 12:
    re = round(float(total_bill * 1.12)/split_bill, 2)
elif tip == 15:
    re = round(float(total_bill * 1.15)/split_bill, 2) 

print(f"Each person should pay: ${re}")
    