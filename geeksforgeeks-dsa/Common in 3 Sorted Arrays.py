def common_element(arr1,arr2,arr3):
#     set1 = set(arr1)
#     set2 = set(arr2)
#     set3 = set(arr3)
#     common_ele = set1 & set2 & set3
#     return sorted(list(common_ele))


        set_b = set(arr2)
        set_c = set(arr3)

        ans = []

        for num in set(arr1):
            if num in set_b and num in set_c:
                ans.append(num)

        return sorted(ans)

arr1 = [1,3,5,9,10,15,24,36]
arr2 = [1,3,5,4,6,8,9,25,46]
arr3 = [1,4,6,9,20,25,36,45]
print(common_element(arr1,arr2,arr3))