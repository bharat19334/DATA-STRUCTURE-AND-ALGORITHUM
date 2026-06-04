def isPalindrome(s):
    result = ""
    for ch in s:
        if ch.isalnum():
            result += ch.lower()
    left = 0
    right = len(result)-1
    while left < right:
        if result[left] != result[right]:
            return False
        left += 1
        right -= 1
    return True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
            