from numpy import full
from copy import deepcopy


# A chess board used for the problem of n-queens, this board does not have regular chess board characteristics
class NQueensBoard:
    def __init__(self, n):
        self._n = n

        # init a board of n rows by n columns
        self._board = full((n, n), False)

        # init slash, backslash and row lookup arrays
        self._slash_lookup = full((n * 2 - 1), False)
        self._backslash_lookup = full((n * 2 - 1), False)
        self._row_lookup = full(n, False)

    def get_board_state(self):
        return deepcopy(self._board)

    def get_size(self):
        return self._n

    def place_queen(self, row, col):
        self._board[row][col] = True
        self._row_lookup[row] = True
        self._slash_lookup[row + col] = True
        self._backslash_lookup[row - col + (self._n - 1)] = True

    def remove_queen(self, row, col):
        self._board[row][col] = False
        self._row_lookup[row] = False
        self._slash_lookup[row + col] = False
        self._backslash_lookup[row - col + (self._n - 1)] = False

    def is_safe(self, row, col):
        # returns true if there's no other queen in the same diagonal, back diagonal or row
        return (
                not self._slash_lookup[row + col] and
                not self._backslash_lookup[row - col + (self._n - 1)] and
                not self._row_lookup[row]
        )

    def print_board(self):
        for i in range(self._n):
            print('--', end='')
        print('')
        for i in range(self._n):
            for j in range(self._n):
                print('Q' if self._board[i][j] else '_', end='|')
            print(' ')
