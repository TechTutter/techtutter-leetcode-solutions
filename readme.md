# LeetCode Solutions

> A collection of algorithmic challenges solved with a focus on clean code, efficiency, and automated workflow.

![LeetCode Total](https://img.shields.io/badge/Solved-97-00b8a3?style=for-the-badge&labelColor=24292e&logo=leetcode) <!-- LEET_COUNT -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Testing](https://img.shields.io/badge/Tests-Pytest-yellow?style=for-the-badge&logo=pytest)

---

## 🛠️ Project Workflow

This repository uses a custom automation system to maintain consistency and speed up the problem-solving process.

### Creation & Setup
To bootstrap a new challenge:
```bash
make exercise "Number. Problem Title"
```

### Development & Testing
Solutions are developed in Python and verified using `pytest`. Environment management is handled by `uv`:
```bash
uv run pytest
```

### Automation
The repository includes a Git pre-commit hook that automatically updates the problem count in the README whenever a new solution is committed.

---

# Topics

List of problems from "Top 150 Interview" + Others extra marked with `*extra`

Quick Link to Paste (internal use) -> - [1.](./leetproblems/)

## Array / Strings
- [88. Merge Sorted Array](./leetproblems/88.%20Merge%20Sorted%20Array/)
- [27. Remove Element](./leetproblems/27.%20Remove%20Element/)
- [26. Remove Duplicates from Sorted Array](./leetproblems/26.%20Remove%20Duplicates%20from%20Sorted%20Array/)
- [80. Remove Duplicates from Sorted Array II](./leetproblems/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II/)
- [169. Majority Element](./leetproblems/169.%20Majority%20Element/)
- [189. Rotate Array](./leetproblems/189.%20Rotate%20Array/)
- [121. Best Time to Buy and Sell Stocks](./leetproblems/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stocks/)
- [122. Best Time to Buy and Sell Stocks II](./leetproblems/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stocks%20II/)
- [55. Jump Game](./leetproblems/55.%20Jump%20Game/)
- [45. Jump Game II](./leetproblems/45.%20Jump%20Game%20II/)
- [274. H-Index](./leetproblems/274.%20H-Index/)
- [380. Insert Delete GetRandom O(1)](./leetproblems/380.%20Insert%20Delete%20GetRandom%20O1/)
- [238. Product of Array Except Self](./leetproblems/238.%20Product%20of%20Array%20Except%20Self/)
- [134. Gas Station](./leetproblems/134.%20Gas%20Station/)
- [135. Candy](./leetproblems/135.%20Candy/)
- [42. Trapping Rain Water](./leetproblems/42.%20Trapping%20Rain%20Water/)
- [13. Roman to Integer](./leetproblems/13.%20Roman%20to%20Integer/)
- [12. Integer to Roman](./leetproblems/12.%20Integer%20to%20Roman/)
- [58. Length of Last Word](./leetproblems/58.%20Length%20of%20Last%20Word/)
- [14. Longest Common Prefix](./leetproblems/14.%20Longest%20Common%20Prefix/)
- [151. Reverse Words in a String](./leetproblems/151.%20Reverse%20Words%20in%20a%20String/)
- [6. Zigzag Conversion](./leetproblems/6.%20Zigzag%20Conversion/)
- [28. Find the Index of The First Occurrence in a String](./leetproblems/28.%20Find%20the%20Index%20of%20The%20First%20Occurrence%20in%20a%20String/)
- [68. Text Justification](./leetproblems/68.%20Text%20Justification/)

- [5. Longest Palindromic Substring](./leetproblems/5.%20Longest%20Palindromic%20Substring/) *extra
- [843. Guess the Word](./leetproblems/843.%20Guess%20the%20Word/) *extra


## Two Pointers
- [125. Valid Palindrome](./leetproblems/125.%20Valid%20Palindrome/)
- [392. Is Subsequence](./leetproblems/392.%20Is%20Subsequence/)
- [167. Two Sum II - Input Array Is Sorted](./leetproblems/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/)
- [11. Container With Most Water](./leetproblems/11.%20Container%20With%20Most%20Water/)
- [15. 3Sum](./leetproblems/15.%203Sum/)

## Sliding Window

- [209. Minimum Size Subarray Sum](./leetproblems/209.%20Minimum%20Size%20Subarray%20Sum/)
- [3. Longest Substring Without Repeating Characters](./leetproblems/3.%20Longest%20Substring%20Without%20Repeating%20Characters/)
- [30. Substring with Concatenation of All Words](./leetproblems/30.%20Substring%20with%20Concatenation%20of%20All%20Words/)
- [76. Minimum Window Substring](./leetproblems/76.%20Minimum%20Window%20Substring/)

## Matrix

- [36. Valid Sudoku](./leetproblems/36.%20Valid%20Sudoku/)
- [54. Spiral Matrix](./leetproblems/54.%20Spiral%20Matrix/)
- [48. Rotate Image](./leetproblems/48.%20Rotate%20Image/)
- [73. Set Matrix Zeroes](./leetproblems/73.%20Set%20Matrix%20Zeroes/)
- [289. Game of Life](./leetproblems/289.%20Game%20of%20Life/)

## Hashmap

- [383. Ransom Note](./leetproblems/383.%20Ransom%20Note/)
- [205. Isomorphic Strings](./leetproblems/205.%20Isomorphic%20Strings/)
- [290. Word Pattern](./leetproblems/290.%20Word%20Pattern/)
- [242. Valid Anagram](./leetproblems/242.%20Valid%20Anagram/)
- [49. Group Anagrams](./leetproblems/49.%20Group%20Anagrams/)
- [1. Two Sum](./leetproblems/1.%20Two%20Sum/)
- [202. Happy Number](./leetproblems/202.%20Happy%20Number/)
- [219. Contains Duplicate II](./leetproblems/219.%20Contains%20Duplicate%20II/)
- [128. Longest Consecutive Sequence](./leetproblems/128.%20Longest%20Consecutive%20Sequence/)

## Intervals

- [228. Summary Ranges](./leetproblems/228.%20Summary%20Ranges/)
- [56. Merge Intervals](./leetproblems/56.%20Merge%20Intervals/)
- [57. Insert Interval](./leetproblems/57.%20Insert%20Interval/)
- [452. Minimum Number of Arrows to Burst Balloons](./leetproblems/452.%20Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons/)

## Stack

- [20. Valid Parentheses](./leetproblems/20.%20Valid%20Parentheses/)
- [71. Simplify Path](./leetproblems/71.%20Simplify%20Path/)
- [155. Min Stack](./leetproblems/155.%20Min%20Stack/)
- [150. Evaluate Reverse Polish Notation](./leetproblems/150.%20Evaluate%20Reverse%20Polish%20Notation/)
- [224. Basic Calculator](./leetproblems/224.%20Basic%20Calculator/)

## Linked List

- [141. Linked List Cycle](./leetproblems/141.%20Linked%20List%20Cycle/)
- [2. Add Two Numbers](./leetproblems/2.%20Add%20Two%20Numbers/)
- [21. Merge Two Sorted Lists](./leetproblems/21.%20Merge%20Two%20Sorted%20Lists/)
- [138. Copy List with Random Pointer](./leetproblems/138.%20Copy%20List%20with%20Random%20Pointer/)
- [92. Reverse Linked List II](./leetproblems/92.%20Reverse%20Linked%20List%20II/)
- [25. Reverse Nodes in k-Group](./leetproblems/25.%20Reverse%20Nodes%20in%20k-Group/)
- [19. Remove Nth Node From End of List](./leetproblems/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/)
- [82. Remove Duplicates from Sorted List II](./leetproblems/82.%20Remove%20Duplicates%20from%20Sorted%20List%20II/)
- [61. Rotate List](./leetproblems/61.%20Rotate%20List/)
- [86. Partition List](./leetproblems/86.%20Partition%20List/)
- [146. LRU Cache](./leetproblems/146.%20LRU%20Cache/)

## Binary Tree General

- [104. Maximum Depth of Binary Tree](./leetproblems/104.%20Maximum%20Depth%20of%20Binary%20Tree/)
- [100. Same Tree](./leetproblems/100.%20Same%20Tree/)
- [226. Invert Binary Tree](./leetproblems/226.%20Invert%20Binary%20Tree/)
- [101. Symmetric Tree](./leetproblems/101.%20Symmetric%20Tree/)
- [117. Populating Next Right Pointers in Each Node II](./leetproblems/117.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II/)
- [114. Flatten Binary Tree to Linked List](./leetproblems/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List/)
- [112. Path Sum](./leetproblems/112.%20Path%20Sum/)
- [129. Sum Root to Leaf Numbers](./leetproblems/129.%20Sum%20Root%20to%20Leaf%20Numbers/)
- [124. Binary Tree Maximum Path Sum](./leetproblems/124.%20Binary%20Tree%20Maximum%20Path%20Sum/)
- [173. Binary Search Tree Iterator](./leetproblems/173.%20Binary%20Search%20Tree%20Iterator/)
- [222. Count Complete Tree Nodes](./leetproblems/222.%20Count%20Complete%20Tree%20Nodes/)

## Binary Tree BFS

- [199. Binary Tree Right Side View](./leetproblems/199.%20Binary%20Tree%20Right%20Side%20View/)
- [637. Average of Levels in Binary Tree](./leetproblems/637.%20Average%20of%20Levels%20in%20Binary%20Tree/)
- [102. Binary Tree Level Order Traversal](./leetproblems/102.%20Binary%20Tree%20Level%20Order%20Traversal/)

## Bit Manipulation

- [67. Add Binary](./leetproblems/67.%20Add%20Binary/)

## Math

- [9. Palindrome Number](./leetproblems/9.%20Palindrome%20Number/)
- [66. Plus One](./leetproblems/66.%20Plus%20One/)

> All numbers checked Until LinkedLists