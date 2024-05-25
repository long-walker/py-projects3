#first program
#let's try to commit this to remote - more change
#last change for the season 1

from random import randint

user_choices_map = {
    'r' : 'rock',
    's' : 'scissors',
    'p': 'paper',
    'rock' : 'rock',
    'scissors' : 'scissors',
    'paper': 'paper',
    'q':'quit',
    'quit': 'quit'
}

keep_playing = True

computer_options = ['rock', 'scissors', 'paper']

while keep_playing:
    user_choice = input("[r]ock, [s]cissors, [p]aper, or Quit? ")
    user_choice = user_choice.lower()
    if user_choice == 'quit' or user_choice == 'q':
        keep_playing = False
        print("The end...")
        break

    user_choice = user_choices_map.get(user_choice)


    computer_choice = computer_options[randint(0,2)]


    if computer_choice == user_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print(f"You win. {user_choice} smashes {computer_choice}")
        else:
            print(f"You lose. {computer_choice} covers {user_choice}")
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print(f"You win. {user_choice} cuts {computer_choice}")
        else:
            print(f"You lose. {computer_choice} smashes {user_choice}")
    else:
        if computer_choice == 'scissors':
            print(f"You lose. {computer_choice} cuts {user_choice}")
        else:
            print(f"You win. {user_choice} covers {computer_choice
                                                   }")
