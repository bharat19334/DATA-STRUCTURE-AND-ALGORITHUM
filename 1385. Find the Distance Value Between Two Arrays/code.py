class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in range(0,len(arr1)):
            Found = False
            for j in range(0,len(arr2)):
                if abs(arr1[i]-arr2[j])<= d:
                    Found = True
                    break
            if not Found:
                count += 1
        return count

                    
        