# Number of Arithmetic Triplets


def triplet(nums,target):
    i = 0
    j = 1
    k = 2
    count = 0
    n = len(nums)
    while k < n:
        if nums[j]-nums[i] > diff:
            i += 1
        elif nums[j]-nums[i] < diff:
            j += 1
        elif nums[k]-nums[j] < diff:
           k += 1 
        elif nums[k]-nums[j] > diff:
            j += 1
        else:
            count += 1
            i += 1
            k += 1
            j += 1
        if i == j:
            j += 1
        elif j == k:
            k += 1
    return count

nums = [0,1,4,6,7,10]
diff = 3
print(triplet(nums,diff))
