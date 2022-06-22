# if, else 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0 

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:      
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0 
        print("Everything's going to be ok. Have a free ride on us!") # 모든 것이 다 된다. 무료로 이용해 보세요!
        
    else:
        bill = 12
        print("Please pay $12.")
    wants_photos = input("DO you want a photo taken? Y or N.")
    if wants_photos == 'Y':
        bill += 3 # bill = bill + 3 와 같다 
    
    print(f"Your final bill is {bill}")
    
else: 
    print("Sorry, you have to grow taller before you can ride.")

    