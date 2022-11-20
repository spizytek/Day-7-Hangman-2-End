#Step 2

import random
import hangman_words
import hangman_art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess_wrong = (word_length-1)
guess_right = 0
stage_cntdwn = (len(stages) - 1)
end_game = False


while end_game != True:
  guess = input("Guess a letter: ").lower()
  #TODO-2: - Loop through each position in the chosen_word;

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        guess_right += 1
        #print(f"guess right: {guess_right}")
        #print(f"word length: {word_length}")
        
  if guess not in chosen_word:
    if(stage_cntdwn >= 0) :
       print(stages[stage_cntdwn])
       stage_cntdwn-=1
    if(stage_cntdwn == 0):
      print("you lose!")
      print(stages[stage_cntdwn])
      end_game = True
  if(guess_right == word_length):
     print("You win!")
     end_game = True
     print(display)    
