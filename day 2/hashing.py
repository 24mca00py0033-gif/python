numbers=[1,2,3,4,1,2,3,4,5,6,7,8,9,5,6,7,7,7,7,8]
hash_maps={}
n=len(numbers)

for i in range(0,n):
    hash_maps[numbers[i]]=hash_maps.get(numbers[i],0)+1
print(hash_maps)