alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Cipher(direction,start_text,shift_amount):
    end_text = ''
    if direction == 'decode':
            shift_amount *= -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += i
    print(f'The {direction}d text is {end_text}')        
# def decrypt(plain_text,shift_amount):
#     decrpted_word = ''
#     for i in text:
#         new_index = alphabet.index(i)-shift_amount
#         i = alphabet[new_index]
#         decrpted_word += i
#     print(f"The decoded text is {decrpted_word}")
from art import logo
print(logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    Cipher(direction=direction,shift_amount=shift,start_text=text)
    answer = input("Do you want to continue Yes or No:\n").lower()
    if answer == 'no':
       should_end = True
       print('Goodbye.')



