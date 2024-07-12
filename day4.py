# day 4 project
import random
print("Welcome to ROCK,PAPER,SCISSOR game")
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
games_images = [rock,paper,scissors]
user_choice = int(input("What do you choose?Type 0 for Rock, 1 for paper and 2 for scissors.\n"))
if user_choice>=3 or user_choice<0:
    print("Invalid choose,You lose!")
else:
    print(games_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(games_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!!!!!!")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice < user_choice:
        print("You win!!!!!!")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice == user_choice:
        print("Its a draw")









# import random

# rand_int=random.randint(1,10)
# print(rand_int)


# rand_float=random.random()
# print(rand_float)

# -------------------------------------------------------------------------------
# names=['sameeksha','shetty','keshav','sharma']
# # names=names_string.split(', ')
# import random
# lenofnames=len(names)
# randomchoice=random.randint(0,lenofnames-1)
# print(f"{names[randomchoice]} is going to buy the meal today!")

# -------------------------------------------------------------------------------------------

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

# ---------------------------------------------------------------------------------------------

# treaure

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map=[line1,line2,line3]
# print("Hiding your treasure! X marks the spot.")
# position=input()
# letter=position[0].lower()

# abc=['a','b','c']
# number_index = int(position[1])-1
# letter_index = abc.index(letter)

# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")


