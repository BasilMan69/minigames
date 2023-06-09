from time import sleep
import os

demo_board = [
    ['X', 'Y', 'Z', 'A', 'C', 'O', 'O'],
    ['X', 'Y', 'Z', 'A', 'C', 'O', 'O'],
    ['X', 'Y', 'Z', 'A', 'C', 'O', 'O'],
    ['X', 'Y', 'Z', 'A', 'C', 'O', 'O'],
    ['X', 'Y', 'Z', 'A', 'C', 'O', 'O']
]


class ConnectFour:
    p1_symbol = 'X'
    p2_symbol = 'O'
    blank = ' '

    def __init__(self):
        self.board = []  # 5x7 board
        self.turn = 1  # 1 is p1, 2 is p2
        for i in range(5):
            self.board.append([self.blank for i in range(7)])

    def closest_playable_square(self, col):
        for i in range(4, -1, -1):
            if self.board[i][col-1] == self.blank:
                return i
        return -1

    def switch_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def add_to_col(self, col):
        if self.closest_playable_square(col) == -1:
            print(
                "Please play your move in a different column. The column {col} is full")
            self.display()
            self.play()
            return
        if self.turn == 1:
            square_to_place = self.p1_symbol
        else:
            square_to_place = self.p2_symbol
        index_to_place = self.closest_playable_square(col)
        self.board[index_to_place][col-1] = square_to_place
        return index_to_place, col-1
    
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
        print(f"Player {self.turn}'s turn.")
        input_col = int(input("Choose a column to move(1->7): "))
        if input_col == 69 : return True
        while input_col not in list(range(1, 8)):
            print(f"Invalid column: {input_col}. Please enter a different column.")
            input_col = int(input("Choose a column to move(1->7): "))
            if input_col == 69 : return True
        row, col = self.add_to_col(input_col)
        self.display()
        game_over = self.has_won(row, col)
        return game_over

    def play(self):  # two players
        self.start()
        game_over = False
        self.display()
        while not game_over:
            game_over = self.play_one_turn()
        print(f"Game Over! Player {self.turn} has won.")

    def has_won(self, row, col):
        count = 1
        square = self.board[row][col]
        # check vertical
        for i in range(1, 4):
            if row-i >= 0 and self.board[row-i][col] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
        for i in range(1, 4):    
            if row+i < 5 and self.board[row+i][col] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
        for i in range(1, 4):    
        # check horizontal
            if col-i >= 0 and self.board[row][col - i] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
        # check diagonal
            # diagonal upleft
        for i in range(1, 4):    
            if row-i >= 0 and col-i >= 0 and self.board[row-i][col - i] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
            # diagonal downright
        for i in range(1, 4):    
            if col+i < 7 and row+i < 5 and self.board[row + 1][col + i] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
            # diagonal downleft
        for i in range(1, 4):    
            if row+i < 5 and col-i >= 0 and self.board[row+i][col - i] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
            # diagonal upright
        for i in range(1, 4):    
            if col+i < 7 and row-i>=0 and self.board[row - i][col + i] == square:
                count += 1
            else:
                count = 1
                break
            if count == 4: return True
        self.switch_turn()
        return False
        

    def display(self):
        os.system('cls||clear')
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
