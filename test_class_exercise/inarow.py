class Game:
    def __init__(self):
        self.board = [[' ']*7 for _ in range(6)]
        self.current_player = 'X'

    def make_move(self, column):
        row = self.get_next_empty_row(column)
        if row is None:
            return False
        self.board[row][column] = self.current_player
        if self.check_win(row, column):
            print(f"{self.current_player} wins!")
            return True
        if self.check_tie():
            print("Tie game!")
            return True
        self.switch_players()
        return False

    def get_next_empty_row(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                return row
        return None

    def check_win(self, row, column):
        return self.check_horizontal_win(row) or self.check_vertical_win(column) \
               or self.check_diagonal_win(row, column)

    def check_horizontal_win(self, row):
        return any(self.board[row][i:i+4] == [self.current_player]*4 for i in range(4))

    def check_vertical_win(self, column):
        return any([self.board[i][column] for i in range(3)] == [self.current_player]*4 for i in range(3))

    def check_diagonal_win(self, row, column):
        return self.check_positive_slope_diagonal_win(row, column) \
               or self.check_negative_slope_diagonal_win(row, column)

    def check_positive_slope_diagonal_win(self, row, column):
        start_row = row - min(row, column)
        start_col = column - min(row, column)
        diagonal = [self.board[start_row+i][start_col+i] for i in range(min(6-start_row, 7-start_col))]
        return any(diagonal[i:i+4] == [self.current_player]*4 for i in range(len(diagonal)-3))

    def check_negative_slope_diagonal_win(self, row, column):
        start_row = row + min(5-row, column)
        start_col = column - min(5-row, column)
        diagonal = [self.board[start_row-i][start_col+i] for i in range(min(start_row+1, 7-start_col))]
        return any(diagonal[i:i+4] == [self.current_player]*4 for i in range(len(diagonal)-3))

    def check_tie(self):
        return all(' ' not in row for row in self.board)

    def switch_players(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'