# def numbers(num):
#     if num == 0: 
#         return
#     print(num)
#     numbers(num - 1)
# numbers(20)

# def numbers(num):
#     if num == 0:
#         return
#     numbers(num - 1)
#     print(num)

# numbers(20)

#paramterized and functional recursion

# def func(sum,i,n):
#     if i>n: 
#         print(sum)
#         return
#     func(sum+i,i+1,n)

# func(0,1,10)

def fun(n):
    if n==1:
        return 1
    return n + fun(n-1)
print(fun(10))



