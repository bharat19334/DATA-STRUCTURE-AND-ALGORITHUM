
def reverse_arr(arr,start,end):
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        return reverse_arr(arr,start+1,end-1)
    return arr

arr = [8,3]
start = 0 
end = len(arr)-1
print(reverse_arr(arr,start,end))      