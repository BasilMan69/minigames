from time import sleep
import os


class ConnectFour:
    name = 'ConnectFour'
    p1_symbol = 'X'
    p2_symbol = 'O'
    blank = ' '

    def __init__(self):
        self.board = []  # 5x7 board
        self.turn = 1  # 1 is p1, 2 is p2
        for i in range(5):
            self.board.append([self.blank for j in range(7)])

    def set_board_to_default(self):
        for i in range(5):
            self.board[i] = [self.blank for j in range(7)]
        self.turn = 1

    def closest_playable_square(self, col):
        for i in range(4, -1, -1):
            if self.board[i][col-1] == self.blank:
                return i
        return -1

    def is_draw(self):
        for i in range(1, 8):
            if self.closest_playable_square(i) != -1:
                return False
        return True

    def switch_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def add_to_col(self, col):
        index_to_place = self.closest_playable_square(col)
        if index_to_place == -1:
            print(f"Please play your move in a different column. The column {col} is full")
            self.display()
            self.play_one_turn()
        if self.turn == 1:
            square_to_place = self.p1_symbol
        else:
            square_to_place = self.p2_symbol
        self.board[index_to_place][col-1] = square_to_place
        return index_to_place

    def start(self):
        print("Starting Connect Four...")
        sleep(0.5)
        print("...")
        sleep(0.5)
        print("...")
        sleep(0.5)
        print("...")
        sleep(0.5)
        print("Hello 2 players to Connect Four.")

    def play_one_turn(self):
        input_col = 0
        while input_col not in list(range(1, 8)):
            print(f"Player {self.turn}'s turn.")
            input_str = input("Choose a column to move(1->7): ")
            try:
                input_col = int(input_str)
            except ValueError:
                pass
            if input_col == 69:
                return True
            print("Please re-enter a valid column number.")
        row = self.add_to_col(input_col)
        self.display()
        game_over = self.has_won(row, input_col - 1)
        return game_over

    def play(self):  # two players
        self.start()
        game_over = False
        self.display()
        while not game_over:
            game_over = self.play_one_turn()
            if self.is_draw():
                print("Game Over! No one wins! It's a draw!")
                self.set_board_to_default()
                choice = ''
                while choice not in ["yes", "no"]:
                    choice = input("Play again?\nYes || No\n").lower()
                if choice == "yes":
                    self.play()
                else:
                    return
        print(f"Game Over! Player {self.turn} has won.")
        self.set_board_to_default()

    def check_vertical(self, row, col):
        square = self.board[row][col]
        count = 1
        for i in range(1, 4):
            if row-i >= 0 and self.board[row-i][col] == square:
                count += 1
            if row+i < 5 and self.board[row+i][col] == square:
                count += 1
            if count >= 4:
                return True
        return False

    def check_horizontal(self, row, col):
        square = self.board[row][col]
        count = 1
        for i in range(1, 4):
            if col-i >= 0 and self.board[row][col-i] == square:
                count += 1
            if col+i < 7 and self.board[row][col+i] == square:
                count += 1
            if count >= 4:
                return True
        return False

    def check_diagonal_upleft_downright(self, row, col):
        square = self.board[row][col]
        count = 1
        for i in range(1, 4):
            if row-i >= 0 and col-i >= 0 and self.board[row-i][col - i] == square:
                count += 1
            if col+i < 7 and row+i < 5 and self.board[row + 1][col + i] == square:
                count += 1
            if count >= 4:
                return True
        return False

    def check_diagonal_downleft_upright(self, row, col):
        square = self.board[row][col]
        count = 1
        for i in range(1, 4):
            if row+i < 5 and col-i >= 0 and self.board[row + i][col - i] == square:
                count += 1
            if col+i < 7 and row+i < 5 and self.board[row - i][col + i] == square:
                count += 1
            if count >= 4:
                return True
        return False

    def has_won(self, row, col):
        if self.check_vertical(row, col) or self.check_horizontal(row, col) or self.check_diagonal_downleft_upright(row, col) or self.check_diagonal_upleft_downright(row, col):
            return True
        self.switch_turn()
        return False

    def display(self):
        # os.system('cls||clear')
        print("""
        CONNECT FOUR
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
-----------------------------                             
""", end='')
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j == 0:
                    print("| ", end='')
                print(self.board[i][j] + " | ", end='')
                if j == len(self.board[i]) - 1:
                    print("""                                 
-----------------------------                                                    
""", end="")
