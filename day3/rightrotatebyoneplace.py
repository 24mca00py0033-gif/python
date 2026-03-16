nums=[5,-2,3,9,0,6,10,17,1]
n=len(nums)
# brutforce is by slicing nums
# right_rotate=nums[-1:]+nums[:-1]
# nums[:]=nums[-1]+nums[0:n-1]
# print(nums)


temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)