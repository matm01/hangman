import random
from words import words
from gallow import gallow


def game():
    word = [char for char in random.choice(words).upper()]
    state = {'mistakes': 0, 'word': word, 'hidden_word': ['_' for _ in word], 'used_letters': [],
             'difficulty': get_difficulty(), 'state': 'start',  'massage': ''}
    print_hangman(**state)

    while True:
        guess = get_letter(state)
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    state['hidden_word'][i] = guess
            if '_' not in state['hidden_word']:
                state['state'] = 'won'
                print_hangman(**state)
                break
            else:
                update_state(state, {'state': 'running', 'massage': 'CORRECT'})
                print_hangman(**state)

        else:
            state['mistakes'] += 1
            if state['mistakes'] < 6 - state['difficulty']:
                update_state(state, {'state': 'running',
                             'massage': 'WRONG', 'used_letters': guess})
                print_hangman(**state)
            else:
                update_state(state, {'state': 'lost', 'massage': ''})
                print_hangman(**state)
                break


def get_difficulty():
    difficulty = input(
        'Choose the number of mistakes u r allowed to make: (3/4/5/6)')
    return 6 - int(difficulty)


def update_state(state, updates):
    for key in updates:
        if key == 'used_letters':
            state['used_letters'].append(updates[key])
        else:
            state[key] = updates[key]


def get_letter(state):
    guess = ''

    while True:

        guess = input('Choose ur letter: ').upper()
        if not guess.isalpha() or len(guess) != 1:
            state['state'] = 'invalid'
            state['massage'] = 'That is not a valid character'
            print_hangman(**state)
        elif guess in state['used_letters']:
            state['state'] = 'invalid'
            state['massage'] = 'U have already tried this character'
            print_hangman(**state)
        elif guess in state['hidden_word']:
            state['state'] = 'invalid'
            state['massage'] = 'U got this one already'
            print_hangman(**state)
        else:
            break

    return guess


def print_hangman(mistakes, difficulty, hidden_word, used_letters, word, state, massage):
    print('\n' * 50)
    if state == 'start':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print('  Let us Beginn!! The word is >>>' + ''.join(hidden_word) + '<<<')
        print(gallow[mistakes + difficulty])
        print('Good luck!!!')
        if massage == 'x':
            print()
    elif state == 'running':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print(f'        That was {massage}!!!   >>>' +
              ''.join(hidden_word) + '<<<')
        print(gallow[mistakes + difficulty])
        print(
            f'U can have {6 - difficulty - mistakes} more mistakes  until u r hanged.')
        print('U have already tried:     >>>' +
              '-'.join(sorted(used_letters)) + '<<<')
    elif state == 'won':
        print('          #######################')
        print('          ##   !!!YOU WON!!!   ##')
        print('          #######################')
        print()
        print('         The word was >>>' + ''.join(word) + '<<<')
        print(gallow[mistakes + difficulty])
        print('U have prevented ur hanging.........for now.')
        print()
    elif state == 'invalid':
        print('          ########################')
        print('          ##      HANGMAN       ##')
        print('          ########################')
        print()
        print(f'      {massage}!!! >>>' + ''.join(hidden_word) + '<<<')
        print(gallow[mistakes + difficulty])
        print(f'U had {mistakes} mistakes so far.')
        print('U have already tried:     >>>' +
              '-'.join(sorted(used_letters)) + '<<<')
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
