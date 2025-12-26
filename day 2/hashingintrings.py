s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_list=[]

for ch in s:
    ascii_code=ord(ch)
    index=ascii_code-97
    hash_list[index]+=1

