# password-generator-start
from operator import le
import random
from traceback import print_tb
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level 
# password = ""
# for char in range(1,nr_letters+1):
#     let = random.choice(letters)
#     password += let

# for i in range(1,nr_symbols+1):
#     num = random.choice(numbers)
#     password += num 

# for sy in range(1, nr_numbers+1):
#     sym = random.choice(symbols)
#     password += sym

# password_fin = random.shuffle(password)
# print(password)


# High level 
password = []
for char in range(1,nr_letters+1):
    let = random.choice(letters)
    password.append(let)

for i in range(1,nr_symbols+1):
    num = random.choice(numbers)
    password.append(num)

for sy in range(1, nr_numbers+1):
    sym = random.choice(symbols)
    password.append(sym)

random.shuffle(password)

password_list = ""
for char in password:
    password_list += char

print(f"Your password is: {password_list}")
