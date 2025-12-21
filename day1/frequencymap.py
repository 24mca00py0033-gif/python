# numbers=[1,2,3,4,1,2,3,4,5,6,7,8,9,5,6,7,7,7,7,8]
# frequency_map={}
# for i in  range(0,len(numbers)):
#     if numbers[i] in frequency_map:
#         frequency_map[numbers[i] ]+=1
#     else:
#         frequency_map[numbers[i]]=1
# print(frequency_map)
# print(frequency_map[7])


#better approach 
numbers=[1,2,3,4,1,2,3,4,5,6,7,8,9,5,6,7,7,7,7,8]
hash_maps={}
n=len(numbers)

for i in range(0,n):
    hash_maps[numbers[i]]=hash_maps.get(numbers[i],0)+1
print(hash_maps)