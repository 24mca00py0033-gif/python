# binjha=[1,2,3,4,5]
# print(binjha)
# print(type(binjha))
# print(len(binjha))
# print(binjha[0])
# print(binjha[-1])
# print(type(binjha[-1]))


# for i in range(0,5):
#     print(binjha[i],end=" ")

# rashmi=["binjha","lububu","cithaphil","nhi"]
# print(rashmi)

# for i in range(len(rashmi)-1,-1,-1):
#     print(rashmi[i],end=" ")


#make your own list and print all the even numbers

# my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for i in range(0,len(my_list)):
#     if my_list[i]%2==0:
#         print(my_list[i],end=" ")
    
# print("\n")

# for abc in my_list:
#     if abc%2!=0:
#         print(abc,end=" ")

#printing the values at even index positions

ruvi=[12,44,1,2,3,0,-5,67,89,23,45]
# for i in range(0,len(ruvi)):
#     if i%2==0:
#         print(ruvi[i],end=" ")

# smallest=ruvi[0]
# largest=ruvi[0]
# for i in range(0,len(ruvi)):
#     if ruvi[i]<smallest:
#         smallest=ruvi[i]
# print(f"\nsmallest number is: {smallest}")
# for i in range(0,len(ruvi)):
#     if ruvi[i]>largest:
#         largest=ruvi[i]
# print(f"largest number is: {largest}")

"""Q104. Write a program that prompts the user to specify the length of a list

and then requests numbers to populate that list. Display the final list as the output."""

# length=int(input("Enter the lenght of the list"))
# my_list=[]

# for i in range(length):
#     num=(input("Enter the number:"))
#     my_list.append(num)
# print("The final list is:",my_list)

#  Create a list and prompt the user for an 'old number' followed by a
# 'new number.' If the 'old number' exists in the list, replace it with the 'new
# number' provided by the use

# mylist=[10,20,30,40,50,60,70,80,90]

# oldnum=int(input("Enter the old number: "))
# newnum=int(input("Enter the new number: "))

# if oldnum in mylist:
#     index=mylist.index(oldnum)
#     mylist[index]=newnum
#     print("Updated list is:",mylist) 

# new_list=[5,10,15,20,25,30,35,40,45,50]
# old_num=int(input("Enter the old number: "))

# for i in range(len(new_list)):
#     print(new_list[i])
#     if new_list[i]==old_num:
#         new_num=int(input("Enter the new number: "))
#         new_list[i]=new_num
#         break
# print("Updated list is:",new_list)

# Ask the user for a number. Then, from a list of numbers, remove all
# the numbers that can be divided by the number the user entered. (Do on
# your own).

# num=int(input("Enter the number "))

# numlist=[12,13,14,15,16,17,18,19,20]


# result=[]

# for i in numlist:
#     if i % num!=0:
#         result.append(i)
# print("The numbers which are not divisible by",num,"are:",result)


# numlist=[numbers for numbers in numlist if numbers % num !=0  ]

# print("The numbers which are not divisible by",num,"are:",numlist)

# # Create a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Remove even numbers
# numbers = [num for num in numbers if num % 2 != 0]

# # Print result
# print("List after removing even numbers:", numbers)


# numbers= [1,2,3,4,5,6,7,8,9,10]
# result=[]

# for i in numbers:
#     if i%2!=0:
#         result.append(i)   
# print("List after removing even numbers:",result)

# Generate a list of at least 10 numbers. Then, create two separate
# lists called 'odd' and 'even.' Put all the odd numbers from the original list
# into the 'odd' list, and all the even numbers into the 'even' list

# list1=[11,22,33,44,55,66,77,88,99,100]
# odd=[]
# even=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Odd numbers:", odd)
# print("Even numbers:", even)


# first_list=[1,2,3,4,5,6,7,8,9,10]
# second_list=[11,12,13,14,15,16,17,18,19,20]
# thirdlist=[]

# for i in first_list:
#     thirdlist.append(i)
# for j in second_list:
#     thirdlist.append(j)
# print("The combined list is:",thirdlist)
# print("\n")

# thirdlist=first_list+second_list
# print("The combined list is:",thirdlist)
# print("\n")

# thirdlist.extend(first_list)
# thirdlist.extend(second_list)
# print("The combined list is:",thirdlist)

# mylist=[1,2,3,4,5,54,4,5,3,34,1,23,45,67,89,90]

# unipue_list=[]
# for num in mylist:
#     if num not in unipue_list:
#         unipue_list.append(num)

# print("Unique list is:", unipue_list)

# unique_list=list(set(mylist))
# print("Unique list is:", unique_list)


# list1=[1,2,3,4,5]

# search=int(input("Enter the number to be searched: "))
# if search in list1:
#     position=list1.index(search)
#     print(f"The number {search} is found at position {position}")
# else:
#     print(f"The number {search} is not found in the list")

# numbers=[10,20,30,40,50,60,70,80,90,100]

# total=sum(numbers)
# avg=total/len(numbers)

# print(avg)

# numbers=[2,2,2,2,3,3,3,3,33,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,55]
# count={}

# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num]=1
# print(count)

# max_element=None
# max_count=0

# for key in count:
#     if count[key]>max_count:
#         max_count=count[key]
#         max_element=key


# numbers=[12,13,14,15,16,17,18,19,20]
# print(numbers)

# numbers[0],numbers[-1]=numbers[-1],numbers[0]
# print(numbers)  

# mid=len(numbers)//2
# print(mid)
# firsthalf=numbers[:mid]
# secondhalf=numbers[mid:]
# print(firsthalf)    
# print(secondhalf)


