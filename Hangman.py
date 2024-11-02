word_list = ['cheeseburger', 'ice cream', 'ladder', 'arsonist', 'school', 'down', 'mitochondria', 'Europe', 'America', 'Mexico', 'secret',
             'spaghetti', 'pasta', 'your mom', 'apples', 'curry', 'rice', 'coffee', 'pizza', 'pancakes', 'bacon', 'eggs', 'bacon',
             'chicken', 'turtle', 'random word', 'Japan', 'another random word','magic', 'spider lilies', 'hollow purple', 'apples', 'pears',
             'grapes','fruits','paper','computer','i dont know what else to put here', 'more words']
word_list = [word.upper() for word in word_list]

#Picks random word from list
import random
word = random.choice(word_list)
letters = [letter for letter in word] #puts chosen letter into list


#Removes spaces from list
while ' ' in letters:
    letters.remove(' ')




def player():
    guess = input("Guess a letter: ").upper()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Please enter a single letter: ").upper()
    return guess

#Keeps track of guesses
guessed_letters = set()


#Keeps track of placement
placements = ["_"] * len(letters)
print(placements)

def check_guess(guess):
    guessed_letters.add(guess)
    if guess in letters:
        print("* * * Good guess! * * *  \n \n")
        for i, letter in enumerate(word):
            if letter == guess:
                placements[i] = guess
    else:
        print("\n Oops! That letter is not in the word.")
        print("\n \n")

def progress():
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print(" ".join(placements)) #Joins the ' _ ' together to form the correct guessed letters

def main():
    while "_" in placements:
        guess = player()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            check_guess(guess)
        progress()
    print("Congratulations! You guessed the word:", word)

main()