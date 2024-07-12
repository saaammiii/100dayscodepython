#day 3 project 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island\n.Your mission is to find the treasure.")
direction=input('You are at a cross road.Where do u want to go ? Type "left" or "right" ').lower()
if direction == "left":
    direction2=input("You've come to a lake. There is a island in the middle of the lake . Type WAIT to wait for a boat. Type SWIM to swim across.").lower()
    if direction2 == 'wait':
        color=input("You have arrived in the island unharmed. There is a house with 3 doors. one red,one yellow and one blue. which color do u choose?").lower()
        if color=='red':
            print("Its a room full of fire, Game over!!!")
        elif color=='yellow':
            print("You found the tresure. You win!!!")
        elif color=='blue':
            print("You entered to room full of beasts, Game over")
        else:
            print("You chase the door that doesnot exists, game over")
    else:
        print("You got attacked by angry trout, Game over!!!")
else:
    print("You fell into a hole....Game over")



# --------------------------------------------------------------------------------------------------------
      

# print("Welcome to rollercoaster!")
# height=int(input("Enter the height in cm?"))
# if height>120:
#     print("Drain out the water")
# else:
#     print("Continue the flow")
# ------------------------------------------------------------------------------------------------------------

# if else if
# height = int(input("Enter the height in cm"))
# if height <120:
#    print("Can ride")
#    age=int(input("Enter the age"))
#    if age<=18:
#     print("pay $7") 
#    else:
#     print("pay $12")
# else:
#     print("Can't ride")
# ------------------------------------------------------------------------------------

# height = int(input("Enter the height in cm"))
# if height <120:
#    print("Can ride")
#    age=int(input("Enter the age"))
#    if age<12:
#     print("pay $5")
#    elif age>=12 and age<18:
#      print("Pay $7")
#    else: 
#      print("Pay $12")
# else:
#     print("Can't ride")
# --------------------------------------------------------------------------------------

# leap year

# year = int(input())
# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")

# ----------------------------------------------------------------------------------

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# bill=0
# if size=='S':
#   bill=15
# elif size=='M':
#   bill=20
# elif size=='L':
#   bill=25

# if add_pepperoni=='Y':
#   if size=='S':
#     bill+=2
#   if size=='M' or size=='L':
#     bill+=3
    
  
# if extra_cheese=='Y':
#   if size=='S' or size=='M' or size=='L':
#     bill+=1

# print("Your final bill is: $"+str(bill)+'.')

# --------------------------------------------------------------------------------------------

# love calculator

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?

# name=name1+name2
# lower_name=name.lower()
# t=lower_name.count('t')
# r=lower_name.count('r')
# u=lower_name.count('u')
# e=lower_name.count('e')
# cnt1=t+r+u+e

# l=lower_name.count('l')
# o=lower_name.count('o')
# v=lower_name.count('v')
# e=lower_name.count('e')
# cnt2=l+o+v+e

# tot=int(str(cnt1)+str(cnt2))
# if tot<10 or tot>90:
#   print(f"Your score is {tot}, you go together like coke and ment.")
# elif tot>40 and tot<50:
#   print(f"Your score is {tot}, you are alright together.")
# else:
#   print(f"Your score is {tot}.")