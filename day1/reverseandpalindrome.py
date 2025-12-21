n=int(input("Enter the number "))
num=n
result=0
while num>0:
    lastdigit=num%10
    result=(result*10)+lastdigit
    num=num//10
    
print("The reverse if number is ",result)

if result==n:
    print("Number is palindrome ")
else:
    print("Result is not palindrome ")