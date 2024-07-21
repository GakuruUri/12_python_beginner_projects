import random
from words import words
from hangman_visuals import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # Randomly choose something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'Lives left and upi have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W- RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives = 1  # Takes away a life if you are wrong
                print('\nYour letter, ', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('Yay! you guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
