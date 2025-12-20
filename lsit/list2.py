squres =[]
for i in range(1,11):
    squres.append(i*i)

print(squres)

squres=[i**2 for i in range (1,11)]
print(squres)


strings=["apple","banana","cherry","date"]

lengts=[len(s) for s in strings]
print(lengts)


olist=["a","b","c"]

repeated=[item *3 for item in olist ]
print(repeated) 

numbers=[ i for i in range(1,21)]

result=[[num,"EVEN" if num %2 ==0 else "ODD"] for num in numbers]

print(result)