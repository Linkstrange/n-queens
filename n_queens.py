# A class  that can solve the n queens problem given a specific board
class Solver:
    def __init__(self, board):
        self.solutions = []

        self._board_size = board.get_size()
        self._board = board

    def solve_n_queens(self, col=0):
        # If all queens are placed add 1 to the solutions and print the board
        if col >= self._board_size:
            self.save_solution(self._board.get_board_state())
            self._board.print_board()
            return
        # Try to place this queen in each row of this column
        for i in range(self._board_size):
            if self._board.is_safe(i, col):
                # place this queen on the board on position i, col
                self._board.place_queen(i, col)
                # recur to place remaining queens
                self.solve_n_queens(col + 1)
                # remove queen to try next position
                self._board.remove_queen(i, col)

    def save_solution(self, board_state):
        self.solutions.append(board_state)

    def get_solutions_count(self):
        return len(self.solutions)
