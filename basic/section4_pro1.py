# 동전 앞면 뒷면 random 출력 
# import random

# random_ht = random.randint(0,1)

# print(random_ht)
# if random_ht == 0:
#     print("Tails")
# else: 
#     print("Heads")

#day-4-2-exercise 
# import random 
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# num_items = len(names)
# random_name = random.randrange(0, num_items-1)
# buy_name = names[random_name]

# print(f"{buy_name} is going to buy the meal today")

#####################################################
# another method
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meal today")


#day-4-3-exercise 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

columns = int(position[0])
row = int(position[1])
map[row-1][columns-1]= "X"


print(f"{row1}\n{row2}\n{row3}")