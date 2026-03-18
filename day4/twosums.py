class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #brut approach 
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j]==target:
        #             return [i,j]    

        #optimal code 
        hash_map={}
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in hash_map:
                return [hash_map[rem],i]
            hash_map[nums[i]]=i    