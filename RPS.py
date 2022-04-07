import random
computer_choice = random.choice(['scissor', 'rock', 'paper'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print("TIE")

elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN, the computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN the computer had ' + computer_choice)
elif user_choice == 'sissors' and computer_choice == 'paper':
    print('WIN the computer had ' + computer_choice)

else:
    print('You lose :( Computer wins :D')

# import random

# roll = random.randint(1,6)

# guess = int(input('Guess the dice roll:\n'))

# if guess == roll:
#     print("Correct! They rolled a " + str(roll))
# else:
#     print("Wrong! They rolled a " + str(roll))