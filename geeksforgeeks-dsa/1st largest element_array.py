def largest_ele(arr):
    largest = arr[0]
        
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        
    return largest
arr=[5,6,2,55,18,24]
print(largest_ele(arr))
