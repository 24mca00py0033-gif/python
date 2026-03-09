class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        
        reversed_x = int(s[::-1])
        if x < 0:
            reversed_x *= -1
       
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x