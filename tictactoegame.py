import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''
total_rounds = 3
round_number = 1
player_score =0
computer_score = 0
# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)

def print_score():
    if (player_score > computer_score):
        print ("Player won " + str(player_score) + " rounds!!")
    elif (player_score< computer_score):
        print ("Computer won " + str(computer_score) + " rounds!!")
    elif (player_score==0 & computer_score==0):
        print("It is a tie :(")
def board_numbers():
    
    for i in range(round_number):
        print_board()
def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
    rounds()
    
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# Thi is the AI for the game
def computer_move():
    move=-1
    # If it can win easily don't care about the other move
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        # If opponent is rying to win block them.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # If none of that works then take one of the stragetrical places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def space_exist():
    return board.count('X') + board.count('O') != 9

def rounds():
    while space_exist():
        print_board()
        player , computer = select_char()
        print('# Make your move ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Invalid number ! Try again !')
            continue
    #
        if won:
            result='*** Congratulations ! You won ! ***'
            player_score+=1
            break
        elif computer_move()[1]:
            result='=== You lose ! =='
            computer_score+=1
            break;
        elif not space_exist  :
            result = " Deuce!"
            computer_score=computer_score
            player_score=player_score

board_numbers()
print_score()
