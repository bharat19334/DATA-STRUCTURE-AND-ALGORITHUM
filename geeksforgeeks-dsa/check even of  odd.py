# using function 

def check_num(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(check_num(-251))

# # using bitmasking

num = 253
if num & 1 == 0:
    print("Even")
else:
    print("odd")
    
# using 1 line 
num = 5
print("even" if num%2==0 else "odd")