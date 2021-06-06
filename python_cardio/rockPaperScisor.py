import random

options = ['Rock', 'Paper', 'Scisors']

player1 = random.randint(0, len(options)-1)
player2 = random.randint(0, len(options)-1)

print('\nPlayer 1: ', options[player1])
print('Player 2: ', options[player2])

if player1 == player2:
    print('\nEmpate')
else:
    if(player1==1 and player2==0):
        print('\nPlayer 1 WINS!')
    if(player1==2 and player2==1):
        print('\nPlayer 1 WINS!')
    if(player1==0 and player2==2):
        print('\nPlayer 1 WINS!')
    if(player1==0 and player2==1):
        print('\nPlayer 2 WINS!')
    if(player1==1 and player2==2):
        print('\nPlayer 2 WINS!')
    if(player1==2 and player2==0):
        print('\nPlayer 2 WINS!')    


