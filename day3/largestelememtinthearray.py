# class Solution:
#     def largest(self, arr):
#         # code here
#         arr.sort()
#         return arr[-1]
        

class Solution:
    def largest(self, arr):
        # code here
        # arr.sort()
        # return arr[-1]
        
        # larges=arr[0]
        larges=float('-inf')
        n=len(arr)
        for i in range (0,n):
            larges=max(larges,arr[i])
        return larges
        
        
        
