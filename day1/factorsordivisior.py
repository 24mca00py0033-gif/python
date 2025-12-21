#brut force
# number=int(input("Enter the number"))
# num=number
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)

# print(result)

#better approach 
# number=int(input("Enter the number"))
# num=number
# result=[]
# for i in range (1,num//2):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print(result)

#optimal approach 
from math import sqrt
number=int(input("Enter the number"))
num=number
result=[]

for i in range(1,int(sqrt(num))+1):
    if num % i ==0:
        result.append(i)
        if (num// i !=i):
            result.append(num//i)
result.sort()

print(result)


