# final project
# secrete auction program

import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')

from day9art import logo
print(logo)

print("Welcome to the secret auction program.")

bids ={}
bidding_finished = False

def find_highest_bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amt=bidding_record[bidder]
        if bid_amt>highest_bid:
            highest_bid = bid_amt
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(bids)
    elif should_continue == "yes":
        clear_screen()