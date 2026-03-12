class Solution:    
    def printNos(self,n):
        #Code here
        if n==0:
            return 
        self.printNos(n-1)
        print(n,end=" ")
n=10
ob=Solution()
ob.printNos(n)