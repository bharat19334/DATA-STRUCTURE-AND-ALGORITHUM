def isValid(s):
    while True:
        if "()" in s:
            s = s.replace("()", "", 1)
        elif "[]" in s:
            s = s.replace("[]", "", 1)
        elif "{}" in s:
            s = s.replace("{}", "", 1)
        else:
            break
        
    return s == ""

s = "(({[]}))"
print(isValid(s))