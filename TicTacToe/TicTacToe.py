class TicTacToe:
    def __init__(self):
        self.board_height
        self.board_width
        self.board
        self.player

    def get_board_size(self):
        try:
            print("Enter board height")
                self.board_height = int(input())
            print("Enter board width")
                self.board_width = int(input())
        except ValueError:
            print("Board size must be a Number")


    def init_board(self, height, width):
        self.board = [[0 for i in height] for i in width]



    def play_tic_tac_toe_game(self):
        set_board size()
        self.init_board(self.board_height,self.board_width)