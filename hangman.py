import random
from words import words
from gallow import gallow

def game():    
    mistakes = 0
    word = [char for char in random.choice(words).upper()]
    hidden_word = ['_' for _ in word]
    used_letters = []
    print_hangman(mistakes, 0, hidden_word, used_letters, word, 'start', '')
    difficulty = get_difficulty()
   
    while True:
        guess = get_letter(mistakes, hidden_word, used_letters, word)            
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    hidden_word[i] = guess
            if '_' not in hidden_word:
                print_hangman(mistakes, difficulty, hidden_word, used_letters, word, 'won', '')
                break
            else:
                print_hangman(mistakes, difficulty, hidden_word, used_letters, word, 'running', 'CORRECT')
        
        else:
            mistakes += 1
            if mistakes < 6 - difficulty:
                used_letters.append(guess)                
                print_hangman(mistakes, difficulty, hidden_word, used_letters, word, 'running', 'a FAIL')
            else:                
                print_hangman(mistakes, difficulty, hidden_word, used_letters, word, 'lost', '')
                break

def get_difficulty():
    difficulty = input('Choose the number of mistakes u r allowed to make: (3/4/5/6)')
    return 6 - int(difficulty)

def get_letter(mistakes, hidden_word, used_letters, word):
    guess = ''    
    
    while True:
        
        guess = input('Choose ur letter: ').upper()        
        if not guess.isalpha() or len(guess) != 1: 
            print_hangman(mistakes, 0, hidden_word, used_letters, word, 'invalid', 'That is not a valid character')        
        elif guess in used_letters: 
            print_hangman(mistakes, 0, hidden_word, used_letters, word, 'invalid', 'U have already tried this character')        
        elif guess in hidden_word:
            print_hangman(mistakes, 0, hidden_word, used_letters, word, 'invalid', 'U got this one already')
        else:
            break

    return guess   

def print_hangman(mistakes, difficulty, hidden_word, used_letters, word, status, string):
    print('\n' * 50)
    if status == 'start':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print('  Let us Beginn!! The word is >>>' + ''.join(hidden_word) + '<<<')
        print(gallow[mistakes + difficulty])
        print('Good luck!!!')
        if string == 'x':
            print()
    elif status == 'running':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print(f'        That was {string}!!!   >>>' + ''.join(hidden_word) + '<<<')
        print(gallow[mistakes + difficulty])
        print(f'U can have {6 - difficulty - mistakes} more mistakes  until u r hanged.' )
        print('U have already tried:     >>>' + '-'.join(sorted(used_letters)) + '<<<')
    elif status == 'won':
        print('          #######################')
        print('          ##   !!!YOU WON!!!   ##')
        print('          #######################')
        print()
        print('         The word was >>>' + ''.join(word) + '<<<')
        print(gallow[mistakes + difficulty])
        print('U have prevented ur hanging.........for now.')
        print()
    elif status == 'invalid':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print(f'      {string}!!! >>>' + ''.join(hidden_word) +'<<<')
        print(gallow[mistakes + difficulty])
        print(f'U had {mistakes} mistakes so far.')
        print('U have already tried:     >>>' + '-'.join(sorted(used_letters)) + '<<<')
    else:
        print('          #######################')
        print('          ##  !!!GAME OVER!!!  ##')
        print('          #######################')
        print()
        print('       The word was >>>' + ''.join(word) + '<<<')
        print(gallow[mistakes + difficulty])
        print('U have been hanged')
        print()  


game()
while input("Play Again? (Y/N) ").upper() == "Y":        
        game()

