# 1st approach

arr1 = [2,5,6,7,1,9]
arr2 = [4,6,9,2,7,8]
l = []
for i in arr1:
    for j in arr2:
        if i==j:
            l.append(i)
print(l)

# 2nd approach
arr1 = [2,5,6,7,1,9]
arr2 = [4,6,9,2,7,8]
set1 = set(arr1)
set2 = set(arr2)
common_element = set1 & set2
print(list(common_element))


# 3rd approach
l = [i for i in arr1 if i in arr2]
print(l)