
def stringpali(str,start,end):
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True
str = "BANANAB"
start = 0
end = len(str)-1   
print(stringpali(str,start,end))    