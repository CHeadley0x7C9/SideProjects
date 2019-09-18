import random


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])






def player_input():
    marker= ''
    while marker != 'X'or marker != 'O':
        marker = (input("Choose marker 'X' or 'O': ")).upper()
        if marker == 'X' or marker =='O':
            break
    player1 = marker
    if player1 =='X':
        player2 ='O'
    else:
        player2='X'
    return[player1,player2]



def place_marker(board, marker, position):
    for i in range(1,10):
        if i == position:
            board[i] = marker
    return board


def win_check(board, mark):
    mark_won= True
    if board[1]==mark==board[2]==board[3]:
        return mark_won
    elif board[4]==mark==board[5]==board[6]:
        return mark_won
    elif board[7]==mark==board[8]==board[9]:
        return mark_won
    elif board[1]==mark==board[5]==board[9]:
        return mark_won
    elif board[3]==mark==board[5]==board[7]:
        return mark_won
    elif board[1]==mark==board[4]==board[7]:
        return mark_won
    elif board[2]==mark==board[5]==board[8]:
        return mark_won
    elif board[3]==mark==board[6]==board[9]:
        return mark_won
    else:
        return not mark_won


def choose_first():
    player = random.randint(1,2)
    return (f'{player}')


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    length_board = 0
    for element in range(1,10):
        if board[element] == 'X' or board[element] =='O':
            length_board+=1
    return length_board == 9

def player_choice(board):
    position = int(input('Choose a position 1-9: '))
    if space_check(board, position) == True:
        return position


def replay():
    answer = input('Would you like to play again? Y or N: ')
    return answer == 'Y'


print('Welcome to Tic Tac Toe!')
while True: 
    board = [" " for element in range(11)]
    display_board(board)
    playerL = player_input()
    first = int(choose_first())
    if first == 2:
        p1 = playerL[1]
        p2 = playerL[0]
    elif(first == 1):
        p1 = playerL[0]
        p2 = playerL[1]
    print(f'Player 1 is {p1} and Player 2 is {p2}')
    print(f'Player {first} will go first')
    turns = 1
    while full_board_check(board) == False:
        if turns%2 ==1:
            pos = player_choice(board)
            if space_check(board,pos)== True:
                place_marker(board,p1,pos)
                display_board(board)
                turns+=1
                if win_check(board,p1) ==True:
                    print(f'{p1} WINS!')
                    break
            else:
                print('Sorry that spot is taken.')
            
        else:
            pos = player_choice(board)
            if space_check(board,pos)== True:
                place_marker(board,p2,pos)
                display_board(board)
                turns+=1         
                if win_check(board,p2)==True:
                    print(f'{p2} WINS!')
                    break
            else:
                print('Sorry that spot is taken.')
    if win_check(board,p1) == win_check(board,p2):
        print('There is a tie!')
    if not replay():
        break
