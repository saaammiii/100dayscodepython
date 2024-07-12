# age = input()124
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# tot_weeks= 90 * 52
# tot_week_lived = int(age) * 52d
# remained= int(tot_weeks) - int(tot_week_lived)
# print(f"You have {remained} weeks left.")


print("Welcome to the Tip Calculator!")
billAmt= input("What was the total bill? $")
tips=input("How much tip would you like to give? 10, 12, or 15?")
splitt= input("How many people to split the bill?")
bill_with_tip = int(tips)/100 * float(billAmt)+float(billAmt)
bill_with_split = bill_with_tip /int(splitt)

bill_with_splits = round(bill_with_split, 2)

print(f"Each person should pay: ${bill_with_splits}")