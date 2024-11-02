
#Question whether player wants to play
def start_menu():
    print("\n Let's play 'ROCK, PAPER, SCISSORS!'")
    menu = input("Start game? \n yes/no: ")
    print("")
    if menu not in 'yes':
        print("")
        print("\n Okay. \n Leaving. . .")
        quit()


#Player chooses an option
def player_input():
    player = input('Choose: rock, paper, scissors: \n \n You Chose: ')
    while player not in ('rock', 'paper', 'scissors'):
        print("Please choose, rock, paper, or scissors")
        player = input('\n Choose: rock, paper, scissors: ')
    return player



#generates computer option randomly
def number_generator():
    import random
    num = random.randrange(1,10)
    return num


#sets computer option
def computer(num):
    if num == 1 or 2 or 3:
        return "rock"
    elif num == 4 or 5 or 6:
        return "paper"
    elif num == 7 or 8 or  9:
        return "scissors"


#determines who wins or who loses
def option(player, computer_choice):
    global wins

    print(f' \n Computer chooses: {computer_choice} \n')
    
    if player == computer_choice:
        print("\n * * * IT'S A TIE! * * * \n")
        
    elif (player == "rock" and computer_choice == "scissors") or \
         (player == "paper" and computer_choice == "rock") or \
         (player == "scissors" and computer_choice == "paper"):
        print("\n * * * YOU WIN! * * * \n")
        wins+=1
        
    else:
        print(" \n * * * YOU LOSE! * * * \n")
    

def win_count():
    global wins
    print("Number of wins:", wins, "\n \n ")


def game_count():
    global games_played
    games_played += 1
    print(" \n \n Total games Played:", games_played)


#asks if player wants to play again
def question_prompt():
    answer = input("\n Would you like to play again? \n yes/no: ")
    if answer == "yes":
       print("\n \n \n")
       game_repeat()
    else:
        quit()


#function that repeats game 
def game_repeat():
    player = player_input()
    print("")
    num = number_generator()
    computer_choice = computer(num)
    option(player, computer_choice)
    game_count()
    win_count()
    question_prompt()



#main function for everything
def main():
    global wins, games_played
    wins = 0
    games_played = 0

    start_menu()


    player = player_input()
    num = number_generator()
    computer_choice = computer(num)
    option(player, computer_choice)
    game_count()
    win_count()
    question_prompt()


main()