import random
from reprlib import clear
import hangman_art
import hangman_words
# another way 
# from hangman_wordds import word_list

print(hangman_art.logo)

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

print(f'Passt, the solution is {chosen_word}')
add = []
word_length = len(chosen_word)

for i in chosen_word:
    add += "_"
## another way
# for i in range(len(chosen_word)):
#     add += "_"

lives = 7


# while "_" in add:
#     guess  = input("Guess a letter:  ").lower()

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             add[position] = letter 
#     print(add)    
    
#     if guess not in chosen_word:
#         lives -= 1 
#         if lives == 0:
#             print("Your lose")
#         print(add)
        
#         if "_" not in add:
#             print("your win")
        



## solution
end_of_games = False

while not end_of_games:
    guess = input("Guess a letter:  ").lower()
    
    clear()
    
    if guess in add:
         print(f"You've already guessed {guess}.")
         
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            add[position] = letter 
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_games = True
            print("Your lose.")     
               
    print(f"{' '.join(add)}")  
    
    if "_" not in add:
        end_of_games = True
        print("your win.")
    
    
    print(hangman_art.stages[lives])