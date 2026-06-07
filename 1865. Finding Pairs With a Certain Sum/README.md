<<<<<<< HEAD
# 1865. Finding Pairs With a Certain Sum

## Problem

You are given two integer arrays `nums1` and `nums2`.

Implement the `FindSumPairs` class:

- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the object with two arrays.
- `void add(int index, int val)` Adds `val` to `nums2[index]`.
- `int count(int tot)` Returns the number of pairs `(i, j)` such that:

nums1[i] + nums2[j] == tot

### Example

Input:
["FindSumPairs", "count", "add", "count"]
[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8]]

Output:
[null,8,null,2]

Explanation:

```python
FindSumPairs pairs = FindSumPairs(
    [1,1,2,2,2,3],
    [1,4,5,2,5,4]
);

pairs.count(7);   # returns 8
pairs.add(3,2);   # nums2 becomes [1,4,5,4,5,4]
pairs.count(8);   # returns 2
```

---

## Approach

Since `nums1` never changes and only `nums2` is updated, we store the frequency of elements of `nums2` in a hash map.

For every element in `nums1`, we find the required complement:

required = tot - num

If that complement exists in `nums2`, we add its frequency to the answer.

For update operations, we update the frequency map accordingly.

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
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self, tot):
        ans = 0
        for num in self.nums1:
            ans += self.freq[tot - num]
        return ans
```

---

## Time Complexity

- add() → O(1)
- count() → O(n)

---

## Space Complexity

- O(m)

---

## Topics

- Hash Map
- Design
- Array
- Counting
- 
=======
# 1865. Finding Pairs With a Certain Sum

## Problem

You are given two integer arrays `nums1` and `nums2`.

Implement the `FindSumPairs` class:

- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the object with two arrays.
- `void add(int index, int val)` Adds `val` to `nums2[index]`.
- `int count(int tot)` Returns the number of pairs `(i, j)` such that:

nums1[i] + nums2[j] == tot

### Example

Input:
["FindSumPairs", "count", "add", "count"]
[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8]]

Output:
[null,8,null,2]

Explanation:

```python
FindSumPairs pairs = FindSumPairs(
    [1,1,2,2,2,3],
    [1,4,5,2,5,4]
);

pairs.count(7);   # returns 8
pairs.add(3,2);   # nums2 becomes [1,4,5,4,5,4]
pairs.count(8);   # returns 2
```

---

## Approach

Since `nums1` never changes and only `nums2` is updated, we store the frequency of elements of `nums2` in a hash map.

For every element in `nums1`, we find the required complement:

required = tot - num

If that complement exists in `nums2`, we add its frequency to the answer.

For update operations, we update the frequency map accordingly.

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
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self, tot):
        ans = 0
        for num in self.nums1:
            ans += self.freq[tot - num]
        return ans
```

---

## Time Complexity

- add() → O(1)
- count() → O(n)

---

## Space Complexity

- O(m)

---

## Topics

- Hash Map
- Design
- Array
- Counting
- 
>>>>>>> 5452906 (Added new DSA problems)
