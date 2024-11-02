

def guess_number():
    import random
    #generates number from 1-100
    secret_number = random.randrange(1,100)
    return secret_number

def player_input():
    #prompts user to guess number
    guess = int(input("Guess a number between 1 and 100: "))
    return guess


def calculations(secret_number, guess):

    if guess < secret_number:
        print("Too low! Try again.")
        guess = player_input()
        calculations(secret_number, guess)
    elif guess > secret_number:
        print("Too high!")
        guess = player_input()
        calculations(secret_number, guess)
    elif guess == secret_number:
        print("Congratulations! You guessed the number!")
        quit()
    



def main():

    number = guess_number()
    num = player_input()
    calculations(number, num)
        

    
main()