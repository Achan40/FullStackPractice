# Rules
# Computer thinks of a 3 digit number with no repeating digits
# Player then guesses a 3 digit number
# Computer then give back clues

# Clues
# Close: guessed correct num in wrong position
# Match: guess correct num in correct position
# Nope: Haven't guessed anything correctly

import random

# Player Guess
def get_guess():
    return list(input('What is your guess: '))

# Computer code
def get_code():
    digits = [str(num) for num in range(10)]

    # Shuffle digits, then grab the first 3
    random.shuffle(digits)
    return digits[:3]

# Generate Clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "Code Cracked!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')

    if clues == []:
        return ["Nope"]
    else:
        return clues

# Game Logic
print("Welcome")

secret_code = get_code()
clue_report = []

while clue_report != "Code Cracked!":
    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
