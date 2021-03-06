## Binary Search
- http://www.geeksforgeeks.org/binary-search/

## Quick Sort
- http://www.geeksforgeeks.org/quick-sort/

## Merge Sort
- http://www.geeksforgeeks.org/merge-sort/

## K-th Smallest / Largest in a sorted array
- http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/

## KMP
- http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/

## Searching for Patterns | Rabin-Karp Algorithm
- http://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/

## Z algorithm
- http://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

## Aho-Corasick Algorithm for Pattern Searching
- http://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/

## Counting Sort
- http://www.geeksforgeeks.org/counting-sort/

## Manacher's Algorithm
- http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
```
 Given a string, find the longest substring which is palindrome.
 O(N^2): start from center, enumerate all
```
- http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/
```
Case 1: L[currentRightPosition] = L[currentLeftPosition] applies when:
 i-left palindrome is completely contained in center palindrome
 i-left palindrome is NOT a prefix of center palindrome
Case 2: L[currentRightPosition] = L[currentLeftPosition] applies when:
 i-left palindrome is prefix of center palindrome (means completely contained also)
 center palindrome is suffix of input string
Case 3: L[currentRightPosition] > = L[currentLeftPosition] applies when:
 i-left palindrome is prefix of center palindrome (and so i-left palindrome is completely contained in center palindrome)
 center palindrome is NOT suffix of input string
Case 4: L[currentRightPosition] > = centerRightPosition – currentRightPosition applies when:
 i-left palindrome is NOT completely contained in center palindrome
```
- Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 3
 O(N)
