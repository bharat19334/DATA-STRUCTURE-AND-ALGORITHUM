# find the index of array element 

def arr_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [1,5,7,3,6,9,4]
target = 7
print(arr_search(arr,target))