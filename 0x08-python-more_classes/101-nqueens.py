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


def board(n):
    """initilize the size"""
    board = []
    for i in range(n):
        board.append([])
    [row.append(' ') for i in range(n) for row in board]
    return board


def copy(board):
    """return copy of the board"""
    if isinstance(board, list):
        return list(map(copy, board))
    return board


def solution(board):
    """return the solution"""
    solution = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 'Q':
                solution.append([x][y])
                break
    return solution


def xout(board, row, coloum):
    """ spot the board
    args:
    board (list): the obard
    row (int): the row
    coloum (int): the coloum
    """
    for x in range(coloum + 1, len(board)):
        board[row][x] == "x"
    for x in range(coloum - 1, -1, -1):
        board[row][x] = "x"
    for y in range(row + 1, len(board)):
        board[y][coloum] = "x"
    for y in range(row - 1, -1, -1):
        board[y][coloum]
    c = coloum + 1
    for y in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[y][c] = "x"
        c = c + 1
    c = coloum - 1
    for y in range(row - 1, -1, -1):
        if c < 0:
            break
        board[y][c]
        c = c - 1
    c = coloum + 1
    for y in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[y][c] = "x"
        c = c + 1
    c = coloum - 1
    for y in range(row + 1, len(board)):
        if c < 0:
            break
        board[y][c] = "x"
        c = c - 1


def solve(board, row, q, sol):
    """solve the puzzle
    args:
    board (list): the board
    row (int): the row
    q (int): the queens
    sol (list): the solution
    """
    if q == len(board):
        sol.append(solution(board))
        return sol
    for x in range(len(board)):
        if board[row][x] == " ":
            c_board = copy(board)
            c_board[row][x] = "Q"
            xout(c_board, row, x)
            sol = solve(c_board, row + 1, q + 1, sol)
    return sol


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = board(int(sys.argv[1]))
    solution = solve(board, 0, 0, [])
    for s in solution:
        print(s)
