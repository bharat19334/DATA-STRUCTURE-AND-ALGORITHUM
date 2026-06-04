def Bubble_sort(nums):
    for i in range(len(nums)-2,0,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
nums = [5,8,1,6,9,2,4]
print(Bubble_sort(nums))
