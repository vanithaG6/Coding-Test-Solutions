a = int(input("Enter a number: "))

if a <= 2:
    total = 1
elif a <= 4:
    total = 3
elif a <= 6:
    total = 5
elif a <= 8:
    total = 7
else:
    total = 9  

num = 1
for i in range(total):
    print(num, end=", " if i < total - 1 else "")
    num += 2
