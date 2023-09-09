from enum import Enum
import numpy as np
import colorama as color


class Connect4Consts(Enum):
    rows: int = 6
    columns: int = 7
    max_turns = rows * columns


class Game_play:

    def __init__(self):
        self.board = np.zeros((Connect4Consts.rows.value, Connect4Consts.columns.value))

    def display_board(self):
        board_str = ''
        for r in range(Connect4Consts.rows.value):
            for c in range(Connect4Consts.columns.value):
                if self.board[r][c] == 0:
                    board_str += '■ '
                elif self.board[r][c] == 1:
                    board_str += (color.Fore.RED + '■ ' + color.Style.RESET_ALL)
                else:
                    board_str += (color.Fore.BLUE + '■ ' + color.Style.RESET_ALL)
            board_str += '\n'
        print(f'\n{board_str}')

    def check_column_vaild(self, column):
        """
        checks if the column is in the range of the board array and if its a int
        :param column:
        :return: True if the column is vaild false otherwise
        """
        if isinstance(column, int) and column in range(Connect4Consts.columns.value):
            return True

    def get_available_row(self, column):
        """
        finding the next available row at the column to place a piece by using a iterating the board
        in reverse order that finds the lowest row available that equals to 0.
        :return: the lowest row in a column that is empty (no piece yet).
        """
        for r in reversed(range(Connect4Consts.rows.value)):
            if self.board[r][column] == 0:
                return r

    def drop_piece(self, row, column, player):
        """
        drops the game piece in the column of the input provided at the available row.
        :return: drops the piece in the available row in the column
        """

        self.board[row][column] = player

    def check_first_row(self, column):
        # checks if the first row is available

        return self.board[0][column] == 0

    def check_for_four(self, player):
        """
        checks if there is 4 values in the same row or colummn in a vertial, horizontal and diagonal way.
        :para2m self.board:
        :param player:
        :return: which player won the game
        """
        # check for horizontal lines
        for c in range(Connect4Consts.columns.value - 3):
            for r in range(Connect4Consts.rows.value):
                if self.board[r][c] == player and self.board[r][c + 1] == player and self.board[r][c + 2] == player \
                        and self.board[r][c + 3] == player:
                    return True

        # check for vertical lines
        for c in range(Connect4Consts.columns.value):
            for r in range(Connect4Consts.rows.value - 3):
                if self.board[r][c] == player and self.board[r + 1][c] == player and self.board[r + 2][c] == player \
                        and self.board[r + 3][c] == player:
                    return True

        # check for diagonal lines
        for c in range(Connect4Consts.columns.value - 3):
            for r in range(Connect4Consts.rows.value - 3):
                if self.board[r][c] == player and self.board[r + 1][c + 1] == player and self.board[r + 2][
                    c + 2] == player \
                        and self.board[r + 3][c + 3] == player:
                    return True

        # check for sloped diagonal lines
        for c in range(Connect4Consts.columns.value - 3):
            for r in range(3, Connect4Consts.rows.value):
                if self.board[r][c] == player and self.board[r - 1][c + 1] == player and self.board[r - 2][
                    c + 2] == player \
                        and self.board[r - 3][c + 3] == player:
                    return True

    def check_draw(self):
        # checks if the board is full
        if np.count_nonzero(self.board) == Connect4Consts.max_turns.value:
            return True

    def player(self, num):
        if num % 2 == 0:
            return 1
        else:
            return 2


game = Game_play()
game.display_board()

for turn in range(Connect4Consts.max_turns.value):
    """
    we do the following:
    1. the user enters the column to put the piece in
    2. the game checks if the column is vaild
    3. the game finds the next available row to place the piece in the column
    4. the game places the piece in the codlumn
    5. passes the turn to the next player
    6. the game checks the columns and rows for a row of 4
    """
    
    while True:
        try:
            column = int(input(f'\nPlayer {game.player(turn)} - Enter your selection (1-{Connect4Consts.columns.value}): ')) - 1
            break
        
        except ValueError:
                print('\nInvalid Value, Try again.')

    while not game.check_column_vaild(column=column):
        try:
            print(f'\nThe column {column + 1} entered is invalid! ')
            column = int(
                input(f'\nPlayer {game.player(turn)} - Enter your selection (1-{Connect4Consts.columns.value}): ')) - 1
        
        except ValueError:
                print('\nInvalid Value, Try again.')

    while not game.check_first_row(column=column):
        try:
            print('\nThe column is full, Try again.')
            column = int(
                input(f'\nPlayer {game.player(turn)} - Enter your selection (1-{Connect4Consts.columns.value}): ')) - 1
            
        except ValueError:
                print('\nInvalid Value, Try again.')

                

    row = game.get_available_row(column=column)
    game.drop_piece(column=column, row=row, player=game.player(turn))

    game.display_board()

    if game.check_for_four(player=game.player(turn)):
        print(f'Player {game.player(turn)} Won!')
        break

    if game.check_draw():
        print('It\'s a Draw!')
        break
