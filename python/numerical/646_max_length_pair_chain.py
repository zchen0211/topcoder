"""
646. Maximum Length of Pair Chain My SubmissionsBack to Contest (Medium)

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""

class Solution(object):
  def findLongestChain(self, pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    n = len(pairs)
    if n == 0: return 0

    pairs.sort(key=lambda item: item[1])
    result = [pairs[0]]
    i = 1
    while i < n:
      if pairs[i][0]>result[-1][1]:
        result.append(pairs[i])
      i += 1
    print result
    return len(result)


if __name__ == '__main__':
  a = Solution()
  print a.findLongestChain([[1,2], [2,3], [3,4]])