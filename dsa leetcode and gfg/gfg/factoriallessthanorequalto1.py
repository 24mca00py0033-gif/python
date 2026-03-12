class Solution:
    def factorialNumbers(self, n):
        ans = []
        fact = 1
        i = 1
        
        while fact <= n:
            ans.append(fact)
            i += 1
            fact = fact * i
            
        return ans