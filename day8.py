# final project

from day8art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(strt_text, shift_amt , direction):
    end_text = ""
    if direction == "decode":
            shift_amt *= -1 
    for char in strt_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amt
            end_text+=alphabet[new_position]
        else:
             end_text+=char
    print(f"The {direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text1 = input("Type your message:\n").lower()
    shift1 = int(input("Type the shift number:\n"))
    shift1 = shift1 % 26
    caesar(strt_text=text1 , shift_amt=shift1,direction=direction1)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
         should_continue = False
         print("Goodbye")



# ===================================================================================================================
# part1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text1 = input("Type your message:\n").lower()
# shift1 = int(input("Type the shift number:\n"))

# def encrypt(text , shift):
#     cipher_text=""
#     for letter in text:
#         position=alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")

# encrypt(text=text1 , shift=shift1)

# =====================================================================================================================
# part2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text1 = input("Type your message:\n").lower()
# shift1 = int(input("Type the shift number:\n"))

# def encrypt(text , shift):
#     cipher_text=""
#     for letter in text:
#         position=alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text , shift):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text+=new_letter
#     print(f"The decoded text is {plain_text}")
    
# if direction1 == "encode":
#     encrypt(text=text1, shift=shift1)
# else:
#     decrypt(cipher_text=text1 , shift=shift1)

# ===========================================================================================================================

# part3

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text1 = input("Type your message:\n").lower()
# shift1 = int(input("Type the shift number:\n"))

# def caesar(strt_text, shift_amt , direction):
#     end_text = ""
#     if direction == "decode":
#             shift_amt *= -1 
#     for letter in strt_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         end_text+=alphabet[new_position]
#     print(f"The {direction}d text is {end_text}")

# caesar(strt_text=text1 , shift_amt=shift1,direction=direction1)

