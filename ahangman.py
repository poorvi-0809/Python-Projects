import random
import hangman_words
from hangman_art import logo, stages



lives = 6


print(logo)
chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    
    if guess in correct_letters:
        print(guess)
        print("You've already chosen this letter.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

   
    if guess not in chosen_word:
        lives -= 1
        print(f"{letter}. You lose a life.")

        if lives == 0:
            game_over = True

           
            print("***********************YOU LOSE**********************")
            print(f"The word is{chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])

    # deal with error