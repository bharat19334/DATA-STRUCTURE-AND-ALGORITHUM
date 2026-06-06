# Common in 3 Sorted Arrays

## Problem

Given three sorted arrays `arr1[]`, `arr2[]`, and `arr3[]` of distinct integers, find all elements that are present in all three arrays.

Return the common elements in sorted order.

If there are no common elements, return an empty array.

---

## Example 1

Input:

arr1 = [1, 5, 10, 20, 40, 80]

arr2 = [6, 7, 20, 80, 100]

arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output:

[20, 80]

Explanation:

20 and 80 are present in all three arrays.

---

## Example 2

Input:

arr1 = [1, 2, 3, 4, 5]

arr2 = [6, 7, 8, 9, 10]

arr3 = [11, 12, 13, 14, 15]

Output:

[]

Explanation:

There is no common element among the three arrays.

---

## Constraints

- 1 ≤ n1, n2, n3 ≤ 10^5
- 1 ≤ arr1[i], arr2[i], arr3[i] ≤ 10^9
- Arrays are sorted in non-decreasing order
