
def solve_n_queen(n):

    def is_safe(row, col, board):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col
                backtrack(row+1, board)
                board[row] = -1

    result = []
    backtrack(0, [-1]*n)
    return result


def print_solutions(solutions):
    for solution in solutions:
        for i in solution:
            row = ["."] * len(solution)
            row[i] = "Q"
            print(" ".join(row))

        print("\n")


if __name__ == '__main__':
    n = 4
    solutions = solve_n_queen(n)
    print_solutions(solutions)
