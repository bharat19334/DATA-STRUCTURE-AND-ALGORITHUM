def intersection(nums1,nums2):
    box = []
    nums1 = set(nums1)
    nums2 = set(nums2)
    for n in nums1:
        if n in nums2:
            box.append(n)
    return box

nums1 = [1,2,3,4,5]
nums2 = [4,5,6,7,9]
print(intersection(nums1,nums2))