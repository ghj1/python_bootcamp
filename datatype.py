#Data Types 

#String 

# print("Hello"[4]) 
# print("123"+"456")

#Integer 

#print(123 + 456)

#Float 
#print(3.14159)

#Boolean 

# True
# False


# 대화형 코딩연습(type)

# two_digit_number = str(input("Type a two digit number: ")) 
# print(int(two_digit_number[0])+int(two_digit_number[1]))

#PEMDASLR (연산 순서) 계산은 항상 왼쪽이 먼저 수행된다.  
# Parentheses ()
# Exponents **
# Multiplication * # Division /
# Addition + # Subtraction - 

# print(3*3+3/3-3) 
# print(3*(3+3)/3-3) 

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# BMI = weight/(height**2)
# print(round(BMI, 0))

# f-String 
# score = 0 
# height = 1.8 
# iswinning = True 

# print(f"your socre is {score}, your height is {height}, you are winning is {iswinning}")


# 대화형 코딩(삶을 주week로 표현하기) # 1년은 365일 52주며 12개월이라는 것 
# age = int(input("what is your current age? "))

# age_days = age * 365 
# age_weeks = age * 52 
# age_months = age * 12 
# d_days = 90*365 - age_days
# d_weeks = 90*52 - age_weeks
# d_months = 90*12 - age_months

# print(f"your have {d_days}days, {d_weeks}weeks and {d_months}months left")

# # 답 
# years_remaining = 90 - age 
# day_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

