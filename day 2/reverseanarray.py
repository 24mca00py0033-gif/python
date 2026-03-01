# def reverse_arr(arr, left, right):
#     if left >= right:  
#         return
#     arr[left], arr[right] = arr[right], arr[left] 
#     reverse_arr(arr, left + 1, right - 1)

arr = [1, 2, 3, 4, 5]
# reverse_arr(arr, 0, len(arr) - 1)
# print(arr)
# print(arr[::-1]) through slicing 

s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_list =[0]*26

for ch in s:
    ascii_code=ord(ch)
    index=ascii_code-97
    hash_list[index]+=1
for ch in q:
    ascii_code=ord(ch)
    index=ascii_code-97
    print(hash_list[index],end=" ")
