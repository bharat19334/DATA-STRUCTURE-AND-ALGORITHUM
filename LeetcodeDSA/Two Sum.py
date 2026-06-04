# 1st approach
def Two_sum(arr,target):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
    return 
arr = [4,-2,5,0,6,3,2,7]
target = 1
print(Two_sum(arr,target))

# 2nd approach
def Twosum(nums,target):
    hash_dict = {}
    for i in range(0,len(nums)):
        hash_dict[nums[i]] = i
        current_num = nums[i]
        required = target - current_num
        if required in hash_dict:
            return [hash_dict[required],hash_dict[current_num]]
nums = [2,7,11,15]
target = 17
print(Twosum(nums,target))
