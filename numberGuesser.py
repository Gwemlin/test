import random
replay = "yes"
correctGuess = "false"
while replay != "no":
    numOfGuesses = 0
    botNum = random.randint(0,10)
    print("I have chosen a number, take a guess!")
    while correctGuess != "true":
        guess = int(input("Guess: "))
        numOfGuesses = numOfGuesses + 1
        if guess == botNum:
            print("You got it!")
            correctGuess = "true"
        elif guess > botNum:
            print("Too high")
        elif guess < botNum:
            print("Too low")
        print("Number of guesses: " + str(numOfGuesses)) 
    print("Thanks for playing")
    correctGuess = "false"
    replay = input("Play again? [yes/no] ")
    