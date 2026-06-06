def getMinMax(arr):
    max = arr[0]
    min = arr[0]
    n = len(arr)
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
    return min,max
arr = [96,8,2,4,6,15,95,35,105,4,7]
print(getMinMax(arr))