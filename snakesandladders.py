import random

def snake_or_ladder(pos):
    # Snakes
    if pos == 61:
        pos = 47
        print('Snake!')
    elif pos == 44:
        pos = 26
        print('Snake!')
    elif pos == 25:
        pos = 10
        print('Snake!')
    elif pos == 18:
        pos = 1
        print('Snake!')
    # Ladders
    elif pos == 3:
        pos = 13
        print('Ladder!')
    elif pos == 11:
        pos = 28
        print('Ladder!')
    elif pos == 30:
        pos = 45
        print('Ladder!')
    elif pos == 42:
        pos = 59
        print('Ladder!')
    return pos

def take_turn(pos):
    global roll
    roll = random.randint(1, 6)
    final_pos = pos + roll
    if final_pos <= 64:
        pos = final_pos
    return pos

player1pos = 1
player2pos = 1
while player1pos and player2pos < 64:
    print('Player 1 is on space {}.'.format(player1pos))
    print('Player 2 is on space {}.'.format(player2pos))
    player1pos = take_turn(player1pos)
    print('Player 1 rolls the die: {}'.format(roll))
    if player1pos == 64:
        print('Player 1 wins!!!')
        break
    player1pos = snake_or_ladder(player1pos)
    print('Player 1 is on space {}.'.format(player1pos))
    print('Player 2 is on space {}.'.format(player2pos))
    player2pos = take_turn(player2pos)
    print('Player 2 rolls the die: {}'.format(roll))
    if player2pos == 64:
        print('Player 2 wins!!!')
        break
    player2pos = snake_or_ladder(player2pos)
