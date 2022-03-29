import random

highest_number = input("Type a number: ")

if highest_number.isdigit():
    highest_number = int(highest_number)

    if highest_number <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, highest_number)
guesses = 0

while True:
    guesses += 1
    player_guess = input("Make a guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Please type a number next time.")
        continue

    if player_guess == random_number:
        print("You got it!")
        break
    elif player_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses.")

