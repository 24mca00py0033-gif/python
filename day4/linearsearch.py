x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target=int(input("Enter the number to search: "))
def linearsearch(x,target):
    for i in range(len(x)):
        if x[i]==target:
            return i    
    return -1
result=linearsearch(x,target)
if result==-1:  
    print("Element not found in the list.")     
else:    
    print("Element found at index:", result)               
