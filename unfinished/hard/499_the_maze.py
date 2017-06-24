"""
499. The Maze II (Hard)

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, your job is to find out how the ball could drop into the hole by moving shortest distance in the maze. The distance is defined by the number of empty spaces the ball go through from the start position (exclude) to the hole (include). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there may have several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and hole coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"
Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)
Output: "impossible"
Explanation: The ball cannot reach the hole.

Note:

1. There are only one ball and one hole in the maze.
2. The ball and hole will only exist in the empty space, and they will not at the same position initially.
3. The given maze doesn't contain border (like the red rectangle in the example pictures), but you should assume the border of the maze are all walls.
4. The maze contains at least 2 empty spaces, and the length and width of the maze won't exceed 30.
"""

class Solution(object):
  def findShortestWay(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """