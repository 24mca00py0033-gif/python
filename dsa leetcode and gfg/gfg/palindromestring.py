# class Solution:
#     def isPalindrome(self, s):
#         # code here 
#         string = s[::-1]
#         if s== string :
#             return True
#         else:
#             return False
        
        
class Solution:
    def isPalindrome(self, s):
        # code here 
        left=0
        right=len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                return False
           
            left+=1
            right-=1
        return 1