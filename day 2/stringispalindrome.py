s="nitin"
n=len(s)
def fun (s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return fun(s,left+1,right-1)

print(fun(s,0,n-1))

    
def reverse_str(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_str(arr, left + 1, right - 1)

def is_palindrome(s):
    return s == s[::-1]  # quick Python check

s = "madam"
arr = list(s)

reverse_str(arr, 0, len(arr) - 1)
reversed_s = "".join(arr)

print("Reversed:", reversed_s)
print("Palindrome:", is_palindrome(s))
