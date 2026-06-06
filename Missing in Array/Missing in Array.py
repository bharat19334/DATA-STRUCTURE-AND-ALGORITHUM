def missingNum(arr):
    l = len(arr)+1
    S = l*(l+1)/2
    
    actual_sum = sum(arr)
    return int(S - actual_sum)
arr = [1,2,3,4,5,6,8,9]
print(missingNum(arr))