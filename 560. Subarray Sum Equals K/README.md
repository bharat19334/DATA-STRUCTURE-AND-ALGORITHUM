# Subarray Sum Equals K

## Problem Statement
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

## Example 1

Input:
nums = [1, 1, 1]
k = 2

Output:
2

Explanation:
The subarrays [1,1] and [1,1] have a sum equal to 2.

## Example 2

Input:
nums = [1, 2, 3]
k = 3

Output:
2

Explanation:
The subarrays [1,2] and [3] have a sum equal to 3.

## Constraints

- 1 <= nums.length <= 2 × 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## Task

Find and return the number of continuous subarrays whose sum is equal to `k`.