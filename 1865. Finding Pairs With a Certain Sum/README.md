# 1865. Finding Pairs With a Certain Sum

## Problem Statement

You are given two integer arrays `nums1` and `nums2`.

Implement the `FindSumPairs` class:

- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the object with two arrays.
- `void add(int index, int val)` Adds `val` to `nums2[index]`.
- `int count(int tot)` Returns the number of pairs `(i, j)` where:

nums1[i] + nums2[j] == tot

### LeetCode Link
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

---

## Approach

### Key Idea
Since `nums1` remains fixed and only `nums2` changes, we can maintain a frequency map for `nums2`.

For every element in `nums1`:

1. Calculate the required value:
   ```
   required = tot - num
   ```
2. Check how many times `required` exists in `nums2`.
3. Add its frequency to the answer.

For update operations:

1. Remove the old value frequency.
2. Update the element.
3. Add the new value frequency.

This allows efficient updates and counting operations.

---

## Algorithm

### add(index, val)

1. Decrease frequency of old value.
2. Update `nums2[index] += val`.
3. Increase frequency of new value.

### count(tot)

1. Initialize answer = 0.
2. Traverse `nums1`.
3. Find complement `(tot - num)`.
4. Add frequency from hash map.
5. Return answer.

---

## Python Solution

```python
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        old = self.nums2[index]
        self.freq[old] -= 1

        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self, tot):
        ans = 0

        for num in self.nums1:
            ans += self.freq[tot - num]

        return ans
```

---

## Example

### Input

```python
nums1 = [1,1,2,2,2,3]
nums2 = [1,4,5,2,5,4]
```

### Operations

```python
count(7)
add(3,2)
count(8)
```

### Output

```python
8
2
```

---

## Time Complexity

### add()
```
O(1)
```

### count()
```
O(n)
```

Where `n = len(nums1)`

---

## Space Complexity

```
O(m)
```

Where `m` is the number of distinct elements in `nums2`.

---

## Topics

- Hash Map
- Design
- Array
- Counting
- Data Structures

---

## Author

**Bharat Goswami**

B.Tech CSE (AI & ML)
