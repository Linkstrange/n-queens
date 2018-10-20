import pytest
import n_queens_solver
import n_queens_board
from timeit import default_timer as timer


# From https://en.wikipedia.org/wiki/Eight_queens_puzzle#Counting_solutions
@pytest.mark.parametrize("n, n_solutions", [
    (1, 1),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724)
])
def test_n_queens(n, n_solutions):
    board = n_queens_board.NQueensBoard(n)
    solver = n_queens_solver.NQueensSolver(board)

    start = timer()
    solver.solve_n_queens()
    end = timer()

    print(f'Elapsed time {end - start} seconds')
    solution_count = solver.get_solutions_count()
    print(f'Expected solutions: {n_solutions}, Got: {solution_count} solutions')
    assert solution_count == n_solutions, "Wrong number of solutions"
    print('Solutions are correct')

