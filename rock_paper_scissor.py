import random
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

print("Choose your option : 0 for Rock, 1 for Paper, 2 for Scissors")
option = int(input())
options_list = [rock, paper, scissors]
print("You chose")
print(options_list[option])
print("Computer chose")
computer_option = random.randint(0, 2)
print(options_list[computer_option])

if option == computer_option:
    print("Its draw")
elif option == 0 and computer_option == 2:
    print("You win")
elif option == 1 and computer_option == 0:
    print("You win")
elif option == 2 and computer_option == 1:
    print("You win")
else:
    print("You lose")
