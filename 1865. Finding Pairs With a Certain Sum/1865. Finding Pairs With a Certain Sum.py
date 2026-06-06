nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [1, 4, 5, 2, 5, 4]

def add(index, val):
    nums2[index] += val

def count(tot):
    ans = 0
    for i in nums1:
        for j in nums2:
            if i + j == tot:
                ans += 1
    return ans

print(count(7))
add(3, 2)
print(nums2)
print(count(8))