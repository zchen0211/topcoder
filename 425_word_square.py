'''
Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 < k < max(numRows, numColumns).

Note:

The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
 

Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
 

Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
 

Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
'''

class Solution(object):
  def WordSquare(self, input_arr):
    Flag = True
    for i in range(len(input_arr)):
      for j in range(i+1, len(input_arr[i])):
        if len(input_arr[j])>=i+1 and input_arr[i][j]==input_arr[j][i]:  # input[i][j] == input[j][i]
          continue
        else:
          return False
      # check ith-column is of len(input_arr[i])
      for j in range(len(input_arr[i]), len(input_arr)):
        if len(input_arr[j]) > i:
          return False
    return True


if __name__ == '__main__':
  a = Solution()
  print a.WordSquare([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"])
  print a.WordSquare(["abcd",
  "bnrt",
  "crm",
  "dt"])
  print a.WordSquare([
  "ball",
  "area",
  "read",
  "lady"])


