<<<<<<< HEAD
# 189. Rotate Array

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

## Example 1

Input:

```python
nums = [1,2,3,4,5,6,7]
k = 3
```

Output:

```python
[5,6,7,1,2,3,4]
```

---

## Example 2

Input:

```python
nums = [-1,-100,3,99]
k = 2
```

Output:

```python
[3,99,-1,-100]
```

---

## Brute Force Solution

The idea is simple:

- Remove the last element of the array.
- Insert it at the beginning.
- Repeat this process `k` times.

For the array:

```python
[1,2,3,4,5,6,7]
```

After 1 rotation:

```python
[7,1,2,3,4,5,6]
```

After 2 rotations:

```python
[6,7,1,2,3,4,5]
```

After 3 rotations:

```python
[5,6,7,1,2,3,4]
```

---

## Python Solution

```python
def rotate(nums, k):
    n = len(nums)

    k = k % n

    for i in range(k):
        last_element = nums.pop()
        nums.insert(0, last_element)

    return nums


nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))
```

---

## Time Complexity

```text
O(k × n)
```

---

## Space Complexity

```text
O(1)
```

---

## Topics

- Array
- Simulation
- Brute Force
=======
# 189. Rotate Array

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

## Example 1

Input:

```python
nums = [1,2,3,4,5,6,7]
k = 3
```

Output:

```python
[5,6,7,1,2,3,4]
```

---

## Example 2

Input:

```python
nums = [-1,-100,3,99]
k = 2
```

Output:

```python
[3,99,-1,-100]
```

---

## Brute Force Solution

The idea is simple:

- Remove the last element of the array.
- Insert it at the beginning.
- Repeat this process `k` times.

For the array:

```python
[1,2,3,4,5,6,7]
```

After 1 rotation:

```python
[7,1,2,3,4,5,6]
```

After 2 rotations:

```python
[6,7,1,2,3,4,5]
```

After 3 rotations:

```python
[5,6,7,1,2,3,4]
```

---

## Python Solution

```python
def rotate(nums, k):
    n = len(nums)

    k = k % n

    for i in range(k):
        last_element = nums.pop()
        nums.insert(0, last_element)

    return nums


nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))
```

---

## Time Complexity

```text
O(k × n)
```

---

## Space Complexity

```text
O(1)
```

---

## Topics

- Array
- Simulation
- Brute Force
>>>>>>> 5452906 (Added new DSA problems)
