# day-3-4-exercise : pizza bill calculation
# print("Welcome to Python Pizza Deliveries!")

# bill = 0 
# size = input("What size pizza do you want? S, M, or L ")
# if size == "S":
#     bill = 15 
# elif size == "M":
#     bill = 20 
# elif size == "L":
#     bill = 25
#     add_pepperoni = input("Do you want pepperoni? Y or N ")
#     if add_pepperoni == "Y":
#         if size == "S":
#             bill += 2
#         elif size == "M" or "L":
#             bill += 3 
#             extra_cheese = input("Do you want extra cheese? Y or N ")
#             if extra_cheese == "Y":
#                 bill += 1 
#                 print(f"Your final bill is: $ {bill}.")
#             elif extra_cheese == "N":
#                  print(f"Your final bill is: $ {bill}.")
# else: 
#     print("Please input size S or M or L")



# day 3-5.exercise : Love calculator 사랑 계산기 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

first_name_lower = name1.lower()
second_name_lower = name2.lower()

T_c = first_name_lower.count("t") + second_name_lower.count("t")
R_c = first_name_lower.count("r") + second_name_lower.count("r")
U_c = first_name_lower.count("u") + second_name_lower.count("u")
E_c = first_name_lower.count("e") + second_name_lower.count("e")

total1 = str(T_c + R_c + U_c + E_c)

L_c = first_name_lower.count("l") + second_name_lower.count("l")
O_c = first_name_lower.count("o") + second_name_lower.count("o")
V_c = first_name_lower.count("v") + second_name_lower.count("v")
E_c2 = first_name_lower.count("e") + second_name_lower.count("e")

total2 = str(L_c + O_c + V_c + E_c2)

Love_Score = total1 + total2

if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and menthos.")
elif Love_Score >= 40 and Love_Score <= 50: 
    print(f"Your score is {Love_Score}, you are alright together.")
else: 
    print(f"Your score is {Love_Score}.")

