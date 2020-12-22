# This is a simple word-guessing game called hangman

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
game_finished = False
lives = len(stages)-1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_finished:
    guess = input("Guess a letter").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the chosen word. You lose a life.")
        lives-=1
        if lives == 0:
            print("You lose")
            game_finished = True
    if not "_" in display:
        game_finished = True
        print("You win")

    print(stages[lives])
