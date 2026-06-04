
def check_sorted(nums):
    for i in range(0,len(nums)-1):
        if nums[i+1] < nums[i]:
            return False
    return True
nums = [1,2,3,4,5,7,8,12,16,17]
print(check_sorted(nums))