def Valid_anagram(s,t):
    hash_dict_1 ={}
    if len(s) != len(t):
        return False
    for i in range(0,len(s)):
        hash_dict_1[s[i]] = hash_dict_1.get(s[i],0)+1
        hash_dict_1[t[i]] = hash_dict_1.get(t[i],0)-1
    for k in hash_dict_1.values():
        if  k != 0:
            return False
    return True
s = "rat"
t = "rat"
print(Valid_anagram(s,t))