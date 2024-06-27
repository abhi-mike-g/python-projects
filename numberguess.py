import random

name = input("Enter name: ")

answer = random.randint(1, 20)
guess_count = 0
max_guesses = 6

while guess_count < max_guesses:
    number = input("Guess the number: ")
    number = int(number)
    guess_count += 1

    if number < answer:
        print("Guess too Low")
    elif number > answer:
        print("Guess too High")
    else:
        break

if number == answer:
    print("Congrats", name, "you guessed correctly in", guess_count, "attempts")
else:
    print("Oops, the number I was thinking of was", answer)
    print("Try Again")
