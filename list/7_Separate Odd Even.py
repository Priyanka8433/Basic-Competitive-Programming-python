A = [1, 2, 3, 4, 5]
for x in A:
    if x % 2 != 0: 
        print(x, end=' ')
print()  
for x in A:   
    if x % 2 == 0:
        print(x, end=' ')
print()

A = [2, 6, 8, 1]
B = []
for x in A:
    B.append(x ** 2)
print(B)
