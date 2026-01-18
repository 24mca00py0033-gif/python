# number=int(input("Enter the number"))

# num =number
# total=0
# numberofdigits=len(str(num))
# while num>0:
#     id =num%10
#     total=total+(id**numberofdigits)
#     num=num//10
# print(total)
# if number==total:
#     print("Number is armstrong")
# else:
#     print("Number is not armstrong")
    
#count digits

# number=int(input("Enter the number "))
# num=number
# count=0
# while num>0:
#     count+=1
#     num=num//10
# print("the no of digits are ",count)

#extraction of digits

# num=23456
# n=num
# while n>0:
#     last_digit=n%10
#     print(last_digit,end=" ")
#     n=n//10

#factors
# number=int(input("Enumbernter the number"))
# num=number
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)
# print(result)

# number=int(input("Enter the number"))
# num=number
# result=[]
# for i in range(1,num//2 + 1):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print(result)

# from math import sqrt
# number=int(input("Enter the number"))
# num=number
# result=[]
# for i in range (1,int(sqrt(num))+1):
#     if num%i==0:
#         result.append(i)
#         if(num// i !=i):
#             result.append(num//i)
# result.sort()
# print(result)
