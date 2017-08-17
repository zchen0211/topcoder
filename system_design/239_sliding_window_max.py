"""
239. Sliding Window Maximum (Hard)

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
import collections

class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 0: return []
    q = collections.deque()
    # init
    for i in range(k):
      while len(q)>0 and q[-1]<nums[i]:
        q.pop()
      q.append(nums[i])
    result = [q[0]]
    # go through
    for i in range(k, len(nums)):
      # remove nums[i-(k-1)]
      if q[0] == nums[i-k]:
        q.popleft()
      # add nums[i]
      while len(q)>0 and q[-1]<nums[i]:
        q.pop()
      q.append(nums[i])
      result.append(q[0])
    return result


if __name__ == '__main__':
  a = Solution()
  print a.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
