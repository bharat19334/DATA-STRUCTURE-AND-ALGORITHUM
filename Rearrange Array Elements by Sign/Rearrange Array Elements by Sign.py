def rearrangeArray(nums):
    positive = []
    nagative = []
    for n in nums:
        if n<0:
            nagative.append(n)
        if n>0:
            positive.append(n)
    ans = []
    i = 0
    while i < len(positive):
        ans.append(positive[i])
        ans.append(nagative[i])
        i += 1
    return ans

nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))