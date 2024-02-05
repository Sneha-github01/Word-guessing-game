import random
import logo_guess
def choose_word():
    words=["python","coding","portfolio","projects","IDE",
         "technical","PyTorch","Data","PyCharm","Flask"]

    return random.choice(words)

def word_status(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_" 
    return display

print(logo_guess.logo)


def word_guessing_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to the guessing game!")
    print("SECRET WORD:", word_status(secret_word,guessed_letters))

    while attempts>0:
        guess = input("Guess a letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter here")
            continue  
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue
        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"No letter {guess} occurs in the word")
            print(f"You have {attempts} chances(s) remining")
        else:
            occurences = secret_word.count(guess) 
            print(f"Letter {guess} occur {occurences} times")

        current_status = word_status(secret_word, guessed_letters)
        print("Secret word:", current_status)

        if "_" not in current_status:
            print("Congratulations! You guessed the right word.") 
            break

    if "_" in current_status:
        print(f"Oops! You've ran out of attempts!")
        print(f"The Secret word was: {secret_word}")      

word_guessing_game()






































#print(word_status("python",["y","h"]))



