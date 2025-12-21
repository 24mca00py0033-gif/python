# results={}
# # while True:
# #     subjet=input("Enter name (or 'done' when to stop) ")
# #     if subjet.lower()=='done':
# #         break
# #     marks=int(input(f"enter marks for{subjet}"))
# #     results[subjet]=marks
# # print("dictionary",results)

# Keys=["maths","english","science","scs","os"]
# values=[1,2,3,4,5]

# my_dictionary=dict(zip(Keys,values))
# print(my_dictionary)

# total_sum=sum(my_dictionary.values())
# print(total_sum)
# total_prod=1
# for val in my_dictionary.values():
#     total_prod*=val
# print(total_prod)
text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1 # If it exists, add 1
    else:
        freq[char] = 1  # If new, start at 1

print(freq)