import n_queens
import queens_board
import dal.mapper as mapper
import dal.n_queens_data_access as data_access
from timeit import default_timer as timer
from sys import argv
from sqlalchemy import exc


def main(n):
    n = int(n)
    solutions_array = []

    start = timer()

    for i in range(n):
        board = queens_board.Board(i + 1)
        solver = n_queens.Solver(board)
        solver.solve_n_queens()
        solutions_array.append(solver.solutions)

    end = timer()

    print(f'Elapsed time {end - start} seconds')

    # Save results to database
    dal = data_access.NQueensDataAccess()

    for i in range(n):
        solutions = solutions_array[i]
        for j in range(len(solutions)):
            mapped_solution = mapper.map_solution(solutions[j], j + 1)
            try:
                dal.save_solution(mapped_solution)
            except exc.IntegrityError:
                dal.rollback()

    dal.finish_session()


if __name__ == "__main__":
    main(argv[1])
