# 가위, 바위, 보 게임 
import random 
game_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_chose = random.randint(0,2)



if game_input == 0:
    print(rock)
    print("Computer chose: ")
    if computer_chose == 0: 
        print(rock)
        print("We are tie")
    elif computer_chose == 1:
        print(paper)
        print("Your lose")
    elif computer_chose == 2:
        print(scissors)
        print("Your win")
elif game_input == 1:
    print(paper)
    print("Computer chose: ")
    if computer_chose == 0: 
        print(rock)
        print("Your win")
    elif computer_chose == 1:
        print(paper)
        print("We are tie")
    elif computer_chose == 2:
        print(scissors)
        print("Your lose")
elif game_input == 2:
    print(scissors)
    print("Computer chose: ")
    if computer_chose == 0: 
        print(rock)
        print("Your lose")
    elif computer_chose == 1:
        print(paper)
        print("Your win")
    elif computer_chose == 2:
        print(scissors)
        print("We are tie")
else:
    print("Your chose 0,1,2")

print("Thist repl has exited, run agin?")


###########################################
# 해설 
game_imges = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice >= 3 or user_choice < 0:
    print("Your typed an invalid number, you lose!")
else:
    print("Your typed an invalid number, you lose!")
    
    print(game_imges[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose: ")
    print(game_imges[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice ==2: 
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
