# 카이사르 암호 
from basic.section8_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encrypt function과 decrypt function을 합치는 caesar() function 만들기 
def caesar(all_text, shift_amount, sel_direction):
    fin_text = ""
    for letter in all_text:
        position = alphabet.index(letter)
        if sel_direction == "encode":
            new_position = position + shift_amount
        elif sel_direction == "decode":
            new_position = position - shift_amount
        fin_text += alphabet[new_position]
    print(f"The {sel_direction} text is {fin_text}")
            

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position  = alphabet.index(letter)
#         new_positon = position + shift_amount
#         cipher_text += alphabet[new_positon]
#     print(f"The encoded text is {cipher_text}")
    
    
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")
    
        
# if direction == "encode":   
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount= shift)

caesar(all_text=text, shift_amount=shift, sel_direction=direction)


# 강사님 solution 
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # if문이 for문 안에 들어갈 경우 반복되는 버그가 생기기 때문에 밖으로 빼줘야 한다. 
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)