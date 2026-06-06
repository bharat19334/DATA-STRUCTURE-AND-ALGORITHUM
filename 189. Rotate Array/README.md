# 189. Rotate Array

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

## Example 1

Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]

Explanation:

1 step rotation:
[7,1,2,3,4,5,6]

2 step rotation:
[6,7,1,2,3,4,5]

3 step rotation:
[5,6,7,1,2,3,4]

---

## Intuition

Instead of shifting elements one by one, we can use the Reverse Technique.

For:

nums = [1,2,3,4,5,6,7]
k = 3

Step 1: Reverse the entire array

[7,6,5,4,3,2,1]

Step 2: Reverse first k elements

[5,6,7,4,3,2,1]

Step 3: Reverse remaining elements

[5,6,7,1,2,3,4]

Final rotated array obtained.

---

## Python Solution

```python
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
```

## Time Complexity

O(n)

## Space Complexity

O(1)

## Topics

- Array
- Two Pointers
- Math
