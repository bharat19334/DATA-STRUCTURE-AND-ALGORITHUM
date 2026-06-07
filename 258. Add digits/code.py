class Solution(object):
    def addDigits(self, num):
        while num>9:
            Total_sum = 0
            while num>0:
                last = num%10
                Total_sum += last
                num = num//10
            num = Total_sum
        return num