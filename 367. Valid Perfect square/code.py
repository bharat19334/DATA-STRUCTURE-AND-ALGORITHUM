class Solution(object):
    def isPerfectSquare(self, num):
        
        root = num**(0.5)
        if int(root) == root:
            return True
        return False