def start_game():
    import random
    import math
    # Receive User input on what numbers to guess between
    low = int(input("Enter Lowest number to guess between: "))

    # Recieve User input on what numbers to guess between
    high = int(input("Enter Highest number to guess between: "))

    # generating random number between the low and high numbers that were inputed
    x = random.randint(low, high)
    print("\n\tYou only have",round(math.log(high - low + 1, 2)),
        "chances to guess the correct number!\n")

    # Initializing the number of guesses
    count = 0

    # for calculation of minimum number of guesses depends upon range
    while count < math.log(high - low + 1, 2):
        count += 1

    # taking guessing number as input
        guess = int(input("Guess a number: "))

    # Condition testing
        if x == guess:
            print("Congratulations! You did it in", count, "tries!")

            # this loop will restart the game and play will continue
            play_again = input("Would you like to play again? (Enter Y / N) ")
            if play_again.upper() == "Y":
                start_game()
            else:
                print("Thanks for playing my game!")
                exit()
            # Once guessed, loop will break
            break
        elif x > guess:
            print("Your guess is too low.")
        elif x < guess:
            print("Your guess is too high.")

    # If guessing is more than required guesses, shows this output.
    if count >= math.log(high - low + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!") 
    # this loop will restart the game and play will continue
    play_again = input("Would you like to play again? (Enter Y / N) ")
    if play_again.upper() == "Y":
        start_game()
    else:
        print("Thanks for playing my game!")
        exit()

# this is where the code starts
start_game()
