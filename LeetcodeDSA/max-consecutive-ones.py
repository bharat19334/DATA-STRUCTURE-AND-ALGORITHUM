def n(nums):
    store = []
    count = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            count +=1
        else:
            count = 0
        store.append(count)
    return max(store)

nums = [1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1]
print(n(nums))