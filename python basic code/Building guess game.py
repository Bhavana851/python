scret_number = 15
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input("Guess:"))
    guess_count += 1
    if guess == scret_number:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("Sorry better luck next time!")
