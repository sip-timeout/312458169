def get_board_size():
    """ Board must be squared and and odd (with one center """
    while True:
        try:
            print("Enter board Size (odd number)")
            board_size = int(input())
        except ValueError:
            print("Board size must be a Number")
            continue
        if(board_size % 2 == 0 ):
            print("Number must be odd")
        # is odd number
        else:
            break
    return board_size


def init_board(board_size):
    """ print blanked board with '0' in each cell """
    board = [[0 for cell in range(0,board_size)] for row in range(0,board_size)]
    return board


def print_board_state(board):
    """ Draw the board after each turn """
    for row in board:
        print(" -"*len(board))
        print("|", end='')
        for cell  in row:
            if cell  == 0:
                print(" ", end='')
            else:
                print(cell , end='')
            print("|",end='')
        print("")
        print(" -"*len(board))


def choose_player(board):
    """ axiom Player X always starts """
    sum_X_on_board = 0
    sum_O_on_board = 0
    for row in board:
        sum_X_on_board += row.count("X")
        sum_O_on_board += row.count("O")
    # out of blanked cells is a Tie
    if((sum_X_on_board+sum_O_on_board) == (len(board)*len(board))):
        print("Game Done it's a Tie")
        sign = "Tie"
    elif(sum_X_on_board <= sum_O_on_board or sum_X_on_board == 0):
        print("Player X turn:")
        sign = "X"
    else:
        print("Player O turn:")
        sign = "O"
    return sign


def play_random_move(board, sign):
    """ choose cell randomly from all the empty places """
    from random import randrange
    x_axis = 0
    y_axis = 0
    empty_pointers = []
    for row in board:
        y_axis = 0
        for cell in row:
            if(cell == 0):
                empty_pointers.append([x_axis,y_axis])
            y_axis+=1
        x_axis+=1
    random_pointer_from_empty = randrange(0,len(empty_pointers))
    # get x_axis and y_axis from the random_pointer and put there sign on board
    board[empty_pointers[random_pointer_from_empty][0]][empty_pointers[random_pointer_from_empty][1]] = sign
    return empty_pointers[random_pointer_from_empty]


def check_winning_move(board, last_move):
    """ Check only around the last move """
    done = check_straight_winning(board, last_move)
    if(not done):
        #Is First/Last row on board
        if(last_move[0] == 0 or last_move[0] == (len(board) - 1)):
            # Corner
            if (last_move[1] == 0 or last_move[1] == (len(board[0]) - 1)):
                done = check_diagonal_winning(board, last_move)
        # Board Center
        elif(last_move[0] == int(len(board)/2) and last_move[1]== int(len(board)/2)):
            done = check_diagonal_winning(board, last_move)
    if(done):
         print("Player {} is the Winner".format(board[last_move[0]][last_move[1]]))
    return done


def check_straight_winning(board, last_move):
    """ only row or column winning """
    done = True
    sign = board[last_move[0]][last_move[1]]
    # Row check
    for cell in range(0,(len(board))):
        # at least one cell not match
        if(not board[last_move[0]][cell] == sign):
            done = False
    # Column check
    if(done == False):
        done = True
        for cell in range(0, (len(board))):
            # at least one cell not match
            if (not board[cell][last_move[1]] == sign):
                done = False
    return done


def check_diagonal_winning(board, last_move):
    """ run only if move is boarder"""
    done = True
    sign = board[last_move[0]][last_move[1]]
    # [0,0] to [last,last]
    for cell in range(0,len(board)):
        if(not board[cell][cell] == sign):
            done = False
    if(not done):
    # [last,o] to [0,last]
        row = len(board)-1
        done = True
        for cell in range(0,len(board)):
            if(not board[row][cell] == sign):
                done = False
            row-=1
    return done




def play_tic_tac_toe_game():
    """ Main """
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
            done = check_winning_move(board, last_move)
        print_board_state(board)



play_tic_tac_toe_game()