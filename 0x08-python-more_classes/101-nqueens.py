#!/usr/bin/python3
"""solving the N queen problem"""
import sys


def checker(col, row, member):
    """check if it could be on the board
    Args:
        col: collumn of the board
        row: row of the board
        member: member of the matrix list
    """
    if row in member:
        return False
    else:
        return all(abs(member[x] - row) != col - x for x in range(col))


def solver(size):
    """solving the n queen
    Args:
        size: size of the board
    """
    result = [[]]
    for x in range(size):
        result = [member + [y] for member in result
                  for y in range(size)
                  if checker(x, y, member)]
    return result


if __name__ == "__main__":
    """check if the number input is valid and print the cordinates"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)
    result = solver(number)
    for member in result:
        new = []
        for i, j in enumerate(member):
            new.append([i, j])
        print(new)
