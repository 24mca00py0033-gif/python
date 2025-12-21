number=int(input("Enter the number"))
num=number
total = 0
numberofdigits=len(str(num))
while num>0:
    id = num%10
    total=total+(id**numberofdigits)
    num=num//10
print(total)
if number==total:
    print("Number is armstrong")
else:
    print("Number is not armastrong")