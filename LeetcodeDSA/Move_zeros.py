# # 1st approach
def Move_zeros(arr):
    insert_index = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[insert_index],arr[i] = arr[i],arr[insert_index] 
            insert_index += 1
    return arr
arr = [1,0,5,0,6,0,4]
print(Move_zeros(arr))

# 2nd approach
def Move_zeros(nums):
    temp = [] * len(nums)
    for i in range(0,len(nums)):
        if nums[i] != 0:
            temp.append(nums[i])
    nums2 = len(temp)
    for i in range(0,nums2):
        nums[i] = temp[i]
    for i in range(nums2,len(nums)):
        nums[i] = 0
    return nums
nums = [0,1,2,5,6,0,0,0,1]
print(Move_zeros(nums))

