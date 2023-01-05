import sys
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

#!/usr/bin/python3

import sys

def solve(N, queens, horizontal, diagonal1, diagonal2):
    if queens == N:
        print(queens)
        return
    for col in range(N):
        if col not in horizontal and queens - col not in diagonal1 and queens + col not in diagonal2:
            horizontal.add(col)
            diagonal1.add(queens - col)
            diagonal2.add(queens + col)
            solve(N, queens+1, horizontal, diagonal1, diagonal2)
            horizontal.remove(col)
            diagonal1.remove(queens - col)
            diagonal2.remove(queens + col)

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(N, 0, set(), set(), set())

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

nqueens(int(sys.argv[1]))
