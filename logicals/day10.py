


""""
Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False if it doesn't.

Examples
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
Notes
Only check for diagonals, horizontals and verticals.

"""

# def bingo_check(board):
#     n = 5
#
#     # Check rows
#     for row in board:
#         if all(cell == "x" for cell in row):
#             return True
#
#     # Check columns
#     for col in range(n):
#         if all(board[row][col] == "x" for row in range(n)):
#             return True
#
#     # Check main diagonal
#     if all(board[i][i] == "x" for i in range(n)):
#         return True
#
#     # Check secondary diagonal
#     if all(board[i][n - 1 - i] == "x" for i in range(n)):
#         return True
#
#     return False
#
#
# print(bingo_check([
#     [67, 43, 31, 74, "x"],
#     [64, "x", 47, "x", 90],
#     [37, 65, "x", 83, 54],
#     [67, "x", 39, "x", 44],
#     ["x", 59, 24, 30, "x"]
# ]))





