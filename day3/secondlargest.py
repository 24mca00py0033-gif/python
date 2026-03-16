nums=[5, 2, 8, 1, 9, 3, 7, 4, 6]
# largest=float('-inf')
# second_largest=float('-inf')

# n=len(nums)
# for i in range (0,n):
#     largest = max(largest,nums[i])
# for i in range (0,n):
#     if nums [i] >second_largest and nums[i] != largest:
#         second_largest=nums[i]
        
# print("Largest element:", largest)
# print("Second largest element:", second_largest)

largest=float('-inf')
second_largest=float('-inf')

for i in range (0,len(nums)):
    if nums[i]>largest:
        second_largest=largest
        largest=nums[i]
    elif nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]

print("Largest element:", largest)
print("Second largest element:", second_largest)
