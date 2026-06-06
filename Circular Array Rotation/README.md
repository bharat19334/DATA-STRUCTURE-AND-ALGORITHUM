# Circular Array Rotation

## Problem

John has found a circular array and wants to perform a number of right circular rotations on it.

For each rotation, the last element of the array becomes the first element.

Given an array, perform `k` right circular rotations and return the values at the specified query indices.

---

## Example

Input:

a = [1, 2, 3]
k = 2
queries = [0, 1, 2]

Output:

[2, 3, 1]

Explanation:

After 1 rotation:

[3, 1, 2]

After 2 rotations:

[2, 3, 1]

Query results:

index 0 → 2

index 1 → 3

index 2 → 1

---

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ k ≤ 10^5
- 1 ≤ q ≤ 500
- 1 ≤ a[i] ≤ 10^5
