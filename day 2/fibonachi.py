def  fu(num):
    if num==0 or num==1:
        return num
    return fu(num-1)+ fu(num-2)

number=int(input("Enter the num for fibonachi "))
fu(number)
print(fu(number))
