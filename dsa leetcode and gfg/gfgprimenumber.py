import math

class Solution:
    def isPrime(self, n: int) -> bool:
        # 1. Base cases
        if n <= 1:
            return False
        if n <= 3:
            return True
            
        # 2. Optimization: Check divisibility by 2 and 3
        if n % 2 == 0 or n % 3 == 0:
            return False
            
        # 3. Loop from 5 up to sqrt(n)
        # We increment by 6 to check 5, 11, 17... and 7, 13, 19...
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True