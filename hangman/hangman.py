import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

#hangman_word_list = ["aardvark", "babbon", "camel"]

chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)
#len_fail_list = len(fail_list)
count = 6
display = []
end_of_game = False
for _ in chosen_word:
  display += "_"
print(logo)
print("Word: ")
print(''.join(display))
print("\n")
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    if guess in display:
      print(f"You already guessed {guess}")
      
    clear()
    if guess in chosen_word:
        for char in range(0, len_chosen_word):
            if chosen_word[char] == guess:
                display[char] = guess
        print(''.join(display))
        if "_" not in display:
            end_of_game = True
            print("You Win")
            break
    else:
        print(stages[count])
        count -= 1
        print(f"Your guess is not in the word, you lose a life guess: {guess}")
        if count == 0:
          end_of_game = True
          print("Game over !! You Lose!! Chosen word was " + chosen_word)



import random
from hangman_words import word_list
from hangman_art import logo, stages

#hangman_word_list = ["aardvark", "babbon", "camel"]

chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)
#len_fail_list = len(fail_list)
count = 6
display = []
end_of_game = False
for _ in chosen_word:
  display += "_"
print(logo)
print("Word: ")
print(''.join(display))
print("\n")
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    if guess in display:
      print(f"You already guessed {guess}")
    
    if guess in chosen_word:
        for char in range(0, len_chosen_word):
            if chosen_word[char] == guess:
                display[char] = guess
        print(''.join(display))
        if "_" not in display:
            end_of_game = True
            print("You Win")
            break
    else:
        print(stages[count])
        count -= 1
        print(f"Your guess is not in the word, you lose a life guess: {guess}")
        if count == 0:
          end_of_game = True
          print("Game over !! You Lose!! Chosen word was " + chosen_word)
