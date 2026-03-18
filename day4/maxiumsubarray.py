class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxi = float("-inf")
        # n = len(nums)
        # for i in range(n):          
        #     s = 0
        #     for j in range(i, n):   
        #         s += nums[j]        
        #         maxi = max(maxi, s) 
        # return maxi

        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range (0,n):
            total=total+nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi