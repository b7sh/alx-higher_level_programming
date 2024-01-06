#!/usr/bin/python3
"""
The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.

attribute:
    board (list): A list representing the board
    solition (list): A list for solution
"""


import sys


def initialize_board(size):
    """initilize the size"""
    return [[' ' for _ in range(size) for _ in range(size)]]


def copy_board(board):
    """return copy of the board"""
    if isinstance(board, list):
        return [copy_board(row) for row in board]
    return board


def get_queen_positions(board):
    """return the solution"""
    position = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 'Q':
                position.append([x, y])
                break
    return position


def mark_attacked_positions(board, row, column):
    """ spot the board
    args:
    board (list): the obard
    row (int): the row
    coloum (int): the coloum
    """
    for x in range(column + 1, len(board)):
        board[row][x] == "x"
    for x in range(column - 1, -1, -1):
        board[row][x] = "x"
    for y in range(row + 1, len(board)):
        board[y][column] = "x"
    for y in range(row - 1, -1, -1):
        board[y][column]
    c = column + 1
    for y in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[y][c] = "x"
        c += 1
    c = column - 1
    for y in range(row - 1, -1, -1):
        if c < 0:
            break
        board[y][c]
        c = c - 1
    c = column + 1
    for y in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[y][c] = "x"
        c += 1
    c = column - 1
    for y in range(row + 1, len(board)):
        if c < 0:
            break
        board[y][c] = "x"
        c -= 1


def solve_n_queens(chess_board, row, queens, solutions):
    """solve the puzzle
    args:
    board (list): the board
    row (int): the row
    q (int): the queens
    sol (list): the solution
    """
    if queens == len(chess_board):
        solutions.append(get_queen_positions(chess_board))
        return solutions
    for x in range(len(chess_board)):
        if chess_board[row][x] == " ":
            copied_board = copy_board(chess_board)
            copied_board[row][x] = "Q"
            mark_attacked_positions(copied_board, row, x)
            solutions = solve_n_queens(
                    copied_board, row + 1, queens + 1, solutions
                    )
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    chess_board = initialize_board(size)
    solution_list = solve_n_queens(chess_board, 0, 0, [])
    for solution in solution_list:
        print(solution)
