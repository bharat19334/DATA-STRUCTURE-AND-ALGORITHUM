class Solution(object):
    def isPowerOfTwo(self, n):
        
        # for i in range(0,n):
        #     if 2**i == n:
        #         return True
        # return False

        if n>0 and (n&(n-1)) == 0:
            return True
        return False