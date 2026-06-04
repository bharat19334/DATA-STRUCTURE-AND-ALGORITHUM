def circularArrayRotation(a, k, queries):
    
    for _ in range(k):
        last = a.pop()
        a.insert(0,last)
    result = []
    for i in queries:
        result.append(a[i])
    return result


a = [3,4,5]
k = 2
queries = [1,2]
print(circularArrayRotation(a,k,queries))