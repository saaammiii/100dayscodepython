# day 7 project

import random

from day7wordlists import word_list

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
end_of_game = False
lives =6

from day7art import logo
print(logo)

display = []
for _ in range(word_len):
    display+="_"

while not end_of_game:
    guess =  input("Enter your guess : ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!!!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!!!!!!!!!!!")

    
    from day7art import stages
    print(stages[lives])

print(f"choosen word is :{chosen_word   }")



# ===========================================================================================================

# hangman part1
# import random
# word_list = ['ardvart', 'baboon', 'camel']
# chosen_word = random.choice(word_list)
# guess = input("ENter your guess?")
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")

# ==========================================================================================

# part2
# import random
# word_list = ['ardvart', 'baboon', 'camel']
# chosen_word = random.choice(word_list)
# print(f"psst, the solution is {chosen_word}. ")

# display_word = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display_word+="_"
# print(display_word)

# guess = input("ENter your guess?").lower()
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display_word[position] = letter

# print(display_word)

# ===================================================================================================

# part3

# import random
# word_list = ['ardvart', 'baboon', 'camel']
# chosen_word = random.choice(word_list)
# print(f"psst, the solution is {chosen_word}. ")

# display_word = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display_word+="_"
# print(display_word)

# end_of_game = False

# while not end_of_game:
#     guess = input("ENter your guess?").lower()
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display_word[position] = letter
#     print(display_word)
    
#     if "_" not in display_word:
#         end_of_game = True
#         print("Win!!!!!!")

# ======================================================================================================================================================
# part4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# lives = 6
# word_list = ['ardvart', 'baboon', 'camel']
# chosen_word = random.choice(word_list)
# print(f"psst, the solution is {chosen_word}. ")

# display_word = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display_word+="_"
# print(display_word)

# end_of_game = False

# while not end_of_game:
#     guess = input("ENter your guess?").lower()


#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display_word[position] = letter
    
#     if guess not in chosen_word:
#         lives-=1
#         if lives == 0:
#             end_of_game = True
#             print("You lose!!!!!")

#     print(display_word)
    
#     if "_" not in display_word:
#         end_of_game = True
#         print("Win!!!!!!")

#     print(stages[lives])