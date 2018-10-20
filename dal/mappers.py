import dal.models as model


def map_placement(board):
    placements = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                placement = model.Placement()
                placement.column = i
                placement.row = j
                placements.append(placement)
    return placements


def map_solution(board, ordinal):
    board_tuple = tuple(map(tuple, board))
    solution = model.Solution()
    solution.board_size = len(board)
    solution.solution_ordinal = ordinal
    solution.board_hash = hash(board_tuple)
    solution.placements = map_placement(board)
    return solution
