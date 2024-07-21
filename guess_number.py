import random


# Computer generated number and the user guesses
def guess(x):
    random_number = random.randint(1, x)
    guess: int = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly.")


# We come up with the secret number and the computer makes the guess.
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay, the computer guessed your number, {guess}, correctly")


computer_guess(1000)

# guess(10)
