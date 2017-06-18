"""
529. Minesweeper (Medium)

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]


Example 2:
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Note:
The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""
import collections

class Solution(object):
  def updateBoard(self, board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    m = len(board)
    n = len(board[0])
    i, j = click
    if board[i][j] == 'M':
      board[i][j] = 'X'
      return board
    tmp = self.neighbor_mine(i,j)
    if tmp == 0:
      board[i][j] = 'B'
      if i>0 and board[i-1][j]=='E': Q.append((i-1,j))
      if i<m-1 and board[i+1][j]=='E': Q.append((i+1,j))
      if j>0 and board[i][j-1]=='E': Q.append((i-1,j))
      if j<n-1 and board[i][j+1]=='E': Q.append((i-1,j))
    else:
      board[i][j] = str(tmp)
    return board

  def neighbor_mine(self, board, i, j):
    m = len(board)
    n = len(board[0])
    cnt = 0
    if i>0 and board[i-1][j] == 'M': cnt += 1
    if i<m-1 and board[i-1][j] == 'M': cnt += 1
    if j>0 and board[i][j-1] == 'M': cnt += 1
    if j<n-1 and board[i][j+1] == 'M': cnt += 1
    if i>0 and j>0 and board[i-1][j-1] == 'M': cnt += 1
    if i>0 and j<n-1 and board[i-1][j+1] == 'M': cnt += 1
    if i<m-1 and j>0 and board[i+1][j-1] == 'M': cnt += 1
    if i<m-1 and j<n-1 and board[i+1][j+1] == 'M': cnt += 1
    return cnt
