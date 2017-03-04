def get_board_size():
    try:
        print("Enter board Size (odd number")
        board_size = int(input())
    except ValueError:
        print("Board size must be a Number")
    return [board_size, board_size]


def init_board(board_size):
    board = [[0 for i in range(0,board_size[1])] for i in range(0,board_size[0])]
    return board


def print_board_state(board):
    for row in board:
        print(" -"*len(board))
        print("|", end='')
        for col in row:
            if col == 0:
                print(" ", end='')
            else:
                print(col, end='')
            print("|",end='')
        print("")
        print(" -"*len(board))


def choose_player(board):
    sumX = 0
    sumO = 0
    for row in board:
        sumX += row.count("X")
        sumO += row.count("O")
    if((sumX+sumO) == (len(board)*len(board))):
        print("Game Done it's a Tie")
        sign = "Tie"
    elif(sumX <= sumO or sumX == 0):
        print("Player X turn")
        sign = "X"
    else:
        print("Player O turn")
        sign = "O"
    return sign


def play_random_move(board, sign):
    from random import randrange
    x = 0
    y = 0
    empty_places = []
    for row in board:
        y = 0
        for col in row:
            if(col == 0):
                empty_places.append([x,y])
            y+=1
        x+=1
    random_place = randrange(0,len(empty_places))
    board[empty_places[random_place][0]][empty_places[random_place][1]] = sign
    return empty_places[random_place]


def check_if_done(board, last_move):
    max_moves = len(board) + len(board[0])
    done = check_straight_winning(board, last_move)
    if(not done):
        # First/Last Col
        if (last_move[0] == 0 or last_move[0] == (len(board) - 1)):
            # Corner
            if (last_move[1] == 0 or last_move[1] == (len(board[0]) - 1)):
                done = check_diagonal_winning(board, last_move)
    if(done):
        print("Player {} is the Winner".format(board[last_move[0]][last_move[1]]))
    return done


def check_straight_winning(board, last_move):
    done = True
    sign = board[last_move[0]][last_move[1]]
    # Row check
    for i in range(0,(len(board))):
        if(not board[last_move[0]][i] == sign):
            done = False
    if(done == False):
        done = True
        for i in range(0, (len(board))):
            if (not board[i][last_move[1]] == sign):
                done = False
    return done


def check_diagonal_winning(board, last_move):
    done = True
    sign = board[last_move[0]][last_move[1]]
    # [0,0] to [last,last]
    for col in range(0,len(board)):
        if(not board[col][col] == sign):
            done = False
    if(not done):
    # [last,o] to [0,last]
        row = len(board)-1
        done = True
        for col in range(0,len(board)):
            if(not board[row][col] == sign):
                done = False
            row-=1
    return done




def play_tic_tac_toe_game():
    done = False
    board_size = get_board_size()
    board = init_board(board_size)
    print_board_state(board)
    while not done:
        sign = choose_player(board)
        if(sign == "Tie"):
            done = True
        else:
            last_move = play_random_move(board, sign)
            done = check_if_done(board, last_move)
        print_board_state(board)



play_tic_tac_toe_game()