a = int(input("Enter percentage: "))

if a < 25:
    print("grade D")
elif a>=25 and a < 45:
     print("grade c")
elif a>=45 and a < 65:
     print("grade B")
elif a>=65 and a < 85:
    print("grade A")
elif a >=85:
     print("grade A+")
else:
    print("fail")    

