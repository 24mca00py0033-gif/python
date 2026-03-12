import math
class Solution:
    def countFactors (self, n):
        # code here
        count=0
        for i in range(1,int(math.sqrt(n))+1):
            if n % i==0:
                if i*i==n:
                    count+=1
                else:
                    count+=2
        return count
            
            