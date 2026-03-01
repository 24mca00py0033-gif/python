s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_list=[0]*26

for ch in s:
    ascii_code=ord(ch)
    index=ascii_code-97
    hash_list[index]+=1
    print(hash_list[index],end=" ")
for ch in q:
    ascii_code=ord(ch)
    index=ascii_code-97
    print(hash_list[index],end=" ")

    
    
