# # # # # # # Ask a number from user. Print all the numbers from 1 to that number
# # # # # # # num=int(input("Enter the number: "))
# # # # # # # i=1
# # # # # # # while i<=num:
# # # # # # #     print(i,end=" ")
# # # # # # #     i=i+1   

# # # # # # Ask start number and end number from user. Print all the numbers
# # # # # # # from start to end using while loop.

# # # # # # start=int(input("Enter the start number: "))
# # # # # # end=int(input("Enter the end number: "))
# # # # # # i=start 
# # # # # # while i<=end:
# # # # # #     print(i,end=" ")
# # # # # #     i=i+1

# # # # # #  Calculate the sum of all the numbers from 1 to 10
# # # # # i=1
# # # # # sum=0
# # # # # while i<10:
# # # # #     sum=sum+i
# # # # #     i=i+1
# # # # # print(f"sum is:  {sum}")  

# # # # # Calculate product of all the numbers from 1 to 10
# # # # i=1
# # # # product=1           
# # # # while i<=10:
# # # #     product=product*i
# # # #     i=i+1
# # # # print(f"Product is: {product}")

# # # # Calculate how many numbers are divisible by 7 from 1 to 100.
# # # i=1
# # # count=0
# # # while i<100:
# # #     if i%7==0:
# # #         count=count+1
# # #     i=i+1
# # # print(f"Number divisible by 7 from 1 to 100 is {count}")

# # # Calculate how many numbers are divisible by both 6 and 7 between 1
# # # to 200.

# # i=1
# # count=0
# # while i<=200:
# #     if i%7 and i%6 ==0:
# #         count=count+1
# #     i=i+1
# # print(f"Number divisible by 6 and 7 from 1 to 200 is {count}")

# # Write a program to calculate the sum of all the numbers divisible by 4
# # from 20 to 50

# i=20
# sum=0

# while i<=50:
#     if i%4==0:
#         print(i,end=" ")
#         sum=sum+i
#         print(f"Sum till now is {sum}")
#     i=i+1
# print(f"Sum of all numbers divisible by 4 from 20 to 50 is {sum}")

# Ask a number from user. Print the multiplication table of that number

num=int(input("Enter the number: "))
i=1
while i<=10:
    print(f"num x {i} ={num*i}")
    i=i+1
