import random


def start_game():
    def guess_number():
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10\n"))
            except ValueError:
                print("That's not a number")
                continue
            else:
                if guess < 1 or guess > 10:
                    print("That's not between 1 and 10")
                    continue
                return guess
     
    high_score = 11
    
    while True:
        random_number = random.randint(1, 10)
        
        print("Welcome to the guessing game!")
        if high_score == 11:
            print("There's no High Score yet.")
        else:
            print("The High Score is: %i" % high_score)
        
        guess = guess_number()
        
        number_of_guesses = 1
        
        while guess != random_number:
            if guess > random_number:
                print("That's too high")
                number_of_guesses += 1
                guess = guess_number()
            else:
                print("That's too low")
                number_of_guesses += 1
                guess = guess_number()
        
        if number_of_guesses == 1:
            print("That's correct, it only took you 1 guess!")
        else:
            print("That's correct! It took you %s guesses" % number_of_guesses)
        
        if number_of_guesses < high_score:
            high_score = number_of_guesses
            
        while True:
            yes_no = input("Would you like to play again? Y/N\n")
            if yes_no.upper() == "Y":
                break
            elif yes_no.upper() == "N":
                print("Goodbye")
                return
            else:
                continue
            
start_game()