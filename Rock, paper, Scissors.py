'''Rock, paper and scissors project'''


import random

def play():
    user = input("Choose your option: 'rock', 'paper', 'scissors'.\n").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return 'Tie'

    if player_wins(user, computer):
        return 'You won'

    return 'You lost'

def player_wins (user, computer):
    # Return True if user wins,
    # Scissors wins to paper (scissors > paper).
    # Paper wins rock (paper > rock).
    # Rock wins to scissors (rock > scissors). 

    if ((user == 'rock' and computer == 'scissors')
        or (user == 'scissors' and computer == 'paper')
        or (user == 'paper' and computer == 'rock')):
        return True
    else:
        return False


print(play())
