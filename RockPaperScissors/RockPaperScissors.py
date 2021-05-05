
import random
games=0
yourwins=0
mywins=0

# print(f'My choice is: {mychoice}')
possible_weapons = ["rock", "paper", "scissors"]
# print(f'Your weapon is: {yourweapon}')
while mywins<3 and yourwins<3:
    yourweapon=input('Which weapon do you choose?(rock,paper,scissors):')
    computer_weapon = random.choice(possible_weapons)
    print(f'My weapon is: {computer_weapon}')
    if yourweapon == computer_weapon:
        print(f"Both players selected {yourweapon}. It's a tie!")
        # break
    elif yourweapon == "rock":
        if computer_weapon == "scissors":
            yourwins= yourwins + 1
            print("Rock smashes scissors! You win!")
            print(yourwins, mywins)
            # break
        else: 
            mywins= mywins + 1
            print("Paper covers rock! You lose.")
            print(yourwins, mywins)
            # break
    elif yourweapon == "paper":
        if computer_weapon == "rock":
            yourwins= yourwins + 1
            print("Paper covers rock! You win!")
            print(yourwins, mywins)
            # break
        else:
            mywins= mywins + 1
            print("Scissors cuts paper! You lose.")
            print(yourwins, mywins)
            # break
    elif yourweapon == "scissors":
        if computer_weapon == "paper":
            yourwins= yourwins + 1
            print("Scissors cuts paper! You win!")
            print(yourwins, mywins)
            # break
        else: 
            mywins= mywins + 1
            print("Rock smashes scissors! You lose.")
            print(yourwins, mywins)
            # break


