def plusOne(digits):
    rev = 0
    for n in digits:
        rev = 10 * rev + n
    new = rev + 1
    box = []
    for i in str(new):
        box.append(int(i))
    return box

digits = [1, 2, 3]
print(plusOne(digits))