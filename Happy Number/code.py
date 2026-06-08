class Solution(object):
    def isHappy(self, n):
        hash_list = []
        while n!= 1:
           
            if n in hash_list:
                return False
            hash_list.append(n)

            store = 0
            while n > 0:

                last = n % 10
                store += last**2
                n = n // 10
            n = store
        return True