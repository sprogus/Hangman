# list of words
# draw lines for number of letters in word
# draw stick figure getting hung

from art import logo, post, head, body, arms, legs
import os

import random
os.system('cls' if os.name == 'nt' else 'clear')


hang_man = {
    0:'',
    1:post,
    2:head,
    3:body,
    4:arms,
    5:legs
}

wordlist = [word for word in (open('words.txt','r').read().splitlines())]
solution = [answer for answer in random.choice(wordlist)]

guess = []

print(logo)
no_guesses = len(solution)
guessed_letters = []
wrong_guess = 0
game_started = False
while no_guesses > 0 and wrong_guess <5:
    
    if not game_started:
        for letter in solution:
            guess.append('_')
            game_started = True
    print(' '.join(guess))
    

    player_guess = input("Guess a letter: ").lower()

    
    valid_guess = False
    if player_guess in guessed_letters: 
        while not valid_guess:
        
            player_guess = input(f"You have already guessed '{player_guess}'. Try another letter: ").lower()
            valid_guess = True

    if player_guess not in solution:
        wrong_guess += 1

    else:    
        guess_index = [n for n,x in enumerate(solution) if x==player_guess]
        for i in guess_index:
            guess[i] = player_guess        
            no_guesses -= 1  
    guessed_letters.append(player_guess)
    print(' '.join(guess))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(hang_man[wrong_guess])
    if wrong_guess == 5:
        print(f"Hangman! The correct word was {''.join(solution)}.")
    elif  no_guesses == 0:
        print(f"You are correct! The word was {''.join(solution)}.")

    