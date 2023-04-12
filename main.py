#Imports
from replit import clear#Only for replit web
import random
import hangman_words
from hangman_words import word_list

#Secret word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False

#Set number of lives
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.

import hangman_art
from hangman_art import logo
from hangman_art import stages
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()#Only for replit web
  
    #User has entered a letter they've already guessed
    if guess in display:
      print(f'You\'ve already guessed "{guess}"')
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'Letter "{guess}" is not in the secret word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. Correct answer was '{chosen_word}'")

    #Join all the elements in the list and turn it into a str.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])