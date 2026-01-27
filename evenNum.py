
count = 0
counta = 0
for i in  range(5,200):
    num = i % 2
    if num == 0:
        count += 1
    else: 
        counta += 1
print("even numbers: ", count)
print("odd numbers: ", counta)


        