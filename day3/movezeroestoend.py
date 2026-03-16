class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # temp=[]

        # for i in range(n):
        #     if nums[i]!=0:
        #         temp.append(nums[i])
        # nz=len(temp)

        # for i in range(nz):
        #     nums[i]=temp[i]

        # for i in range (nz,n):
        #     nums[i]=0
        
        if len(nums)==1:
            return 
        i=0
        while i <len(nums):
            if nums[i]==0:
                break
            i+=1
        else :
            return 
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
