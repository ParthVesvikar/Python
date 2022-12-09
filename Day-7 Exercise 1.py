import random
from hangman_words import word
from hangman_art import logo,stages
print(logo)
choosen_word = random.choice(word)
print(choosen_word)
lives = 6 

display = []
for letter in range(len(choosen_word)):
    display+="_"
#print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter :").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] =letter
    if guess not in choosen_word:
        lives -= 1
    
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"Lives left{lives}")
    print(f'{" ".join(display)}')

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])

