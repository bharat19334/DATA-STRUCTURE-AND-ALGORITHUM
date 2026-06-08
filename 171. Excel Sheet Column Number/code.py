class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0

        for char in columnTitle:
            num = ord(char)-64
            result = result * 26 + num
        return result 