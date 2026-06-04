def rotate(nums, k):
    n = len(nums)
    k = k%n
    for i in range(0,k):
        a = nums.pop()
        nums.insert(0,a)
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))