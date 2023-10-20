#2
C = 18.5
F = -4
print(f'{C} is {round(C*(9/5)+32,1)} F')
print(f'{F} is {round((F-32)*(5/9),1)} C')

#5
firstname = input("First name -")
lastname = input("Last name -")
print(f'{lastname} {firstname}')

#8
from datetime import timedelta

day = int(input('Day - '))
month = int(input('Month - '))
year = int(input('Year - '))

birthdate = datetime.datetime(year, month, day)

currentdate = datetime.datetime.now()

days = (currentdate - birthdate).days


print(f'Total number of days from birth - {days}')

#11
power = int(input('Power -'))

print(2**power)
print(str(2**power)[-2:])

#14
import random
game = ["rock", "paper", "scissors"]
player = 0
bot = 0

for _ in range(3):
    player_choice = input("Type: ")

    bot_choice = random.choice(game)
    print(f"Bot chose {bot_choice}")

    if player_choice == bot_choice:
        print("Tie")
    elif ((player_choice == "rock" and bot_choice == "scissors")
        or (player_choice == "paper" and bot_choice == "rock")
        or (player_choice == "scissors" and bot_choice == "paper")):
        print("You won")
        player += 1
    else:
        print("You lost")
        bot += 1

print(f"Your Score: {player}")
print(f"Bot Score: {bot}")

if player > bot:
    print("You won the game")
elif bot > player:
    print("You lost the game")
else:
    print("Tie")

#17
from datetime import datetime, timedelta

day
month
year =

date1 = datetime(2023, 9, 1)
date2 = datetime.now()
business_days = 0

current_date = date1
while current_date <= date2:
    if current_date.weekday() < 5 and current_date:
        business_days += 1
    current_date += timedelta(days=1)

print(f"Number of business days between {date1.date()} and {date2.date()} is {business_days} days")

#20
def str_remover(input_list):
    return list(filter(None, input_list))

list1 = ["gr432", "", "321", "g4", "", "listsss"]
list2 = str_remover(list1)
print(list1)
print(list2)

#23
dict = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e': 90}

max_number = max(dict.values())
max_key = [key for key, number in dict.items() if number == max_number]

print(f"Maximum value is: {max_key}")

#26
s = input('s = ')
t = input('t = ')

if sorted(s) == sorted(t):
    print(f"True")
else:
    print(f"False")

#29
