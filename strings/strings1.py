# stringfromuser= "binjha  "

# alphabets=[char for char in stringfromuser if char.isalpha()]
# print(len(alphabets))

# string1=input(" Enter the string ")

# uppercount=0
# lowercount=0

# for char in string1:
#     if char.isupper():
#         uppercount+=1
#     elif char.islower():
#         lowercount+=1

# print(uppercount)
# print(lowercount)
# print(string1.upper())
# string2="SSSSS"
# print(string2.lower())\

# string3="I love rashmi"
# words=string3.split()
# print(words)
# reverse=words[::-1]
# print(reverse)
# result=" ".join(reverse)
# print(result)

# text = input("Enter a sentence: ")
# result = " ".join(text.split()[::-1])
# print(result)


sentence = input("Enter a sentence: ")

# 1. Split into words: ["Hello", "World"]
words = sentence.split()

# 2. Reverse letters in each word: ["olleH", "dlroW"]
reversed_word_list = [word[::-1] for word in words]

# 3. Join them back with spaces: "olleH dlroW"
result = " ".join(reversed_word_list)

print("Result:", result)


