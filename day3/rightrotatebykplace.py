class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
         n = len(nums)
         k %= n  
         self.reverse(nums, n - k, n - 1)
         self.reverse(nums, 0, n - k - 1)
         self.reverse(nums, 0, n - 1)
         
    def reverse(self, nums: List[int], l: int, r: int) -> None:

        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]
 
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        rotations=k%n

        for _ in range (0,rotations):
            e=nums.pop()
            nums.insert(0,e)        


        
        
    
       