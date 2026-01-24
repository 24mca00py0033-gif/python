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
# n=int(input("Enter the number "))
# num=n
# result=0
# while num>0:
#     lastdigit=num%10
#     result=(result*10)+lastdigit
#     num=num//10
    
# print("The reverse if number is ",result)

# if result==n:
#     print("Number is palindrome ")
# else:
#     print("Result is not palindrome ")


# numbers=[1,2,3,4,1,2,3,4,5,6,7,8,9,5,6,7,7,7,7,8]
# freqency_map={}
# for i in range(0,len(numbers)):
#     if numbers[i] in freqency_map:
#         freqency_map[numbers[i]]+=1
#     else:
#         freqency_map[numbers[i]]=1 
# print(freqency_map)
# print(freqency_map[7])

#better approach 
# numbers=[1,2,3,4,1,2,3,4,5,6,7,8,9,5,6,7,7,7,7,8]
# hash_maps={}
# n=len(numbers)

# for i in range(0,n):
#     hash_maps[numbers[i]]=hash_maps.get(numbers[i],0)+1
# print(hash_maps)

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# for num in m:
#     count=0
#     for x in n:
#         if x==num:
#             count+=1
#         print(count)
#     print(f"Number {num} occours {count} times in the list n")

# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]
# hash_list=[]
# hash_list=[0]*11
 
# for num in n:
#     hash_list[num]+=1
#     print(hash_list)
# for num in m:
#     if num<1 or num >10:
#         print(0)
#     else:
#         print(hash_list[num],end=" ")


# s="azyxyyzaaaa"
# q=["d","a","y","x"]
# hash_list=[0]*26

# for ch in s:
#     ascii_code=ord(ch)
#     index=ascii_code-97
#     hash_list[index]+=1
# for ch in q:
#     ascii_code=ord(ch)
#     index=ascii_code-97
#     print(hash_list[index],end=" ")
    
# def numbers(num):
#     if num == 0: 
#         return
#     print(num)
#     numbers(num - 1)
# numbers(20)

def numbers(num):
    if num == 0:
        return
    numbers(num - 1)
    print(num,end=" ")

numbers(20)
