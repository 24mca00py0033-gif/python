nums=[1,2,4,5,6]
n=len(nums)
# for i in range(0,n+1):
#     if i not in nums:
#         print(i)
        
#using dictionary
# freq={}
# for i in range(0,n+1):
#     freq[i]=0

# for i in nums:
#     freq[i]=1
# for k,v in freq.items():
#     if v==0:
#         print(k)

#using optimal solution

original_total = (n * (n + 1)) // 2
actual_total = sum(nums)
missing_number = original_total - actual_total
print("The missing number is:", missing_number)