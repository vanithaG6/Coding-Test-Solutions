a = int(input("Enter a number: "))

for i in range(1, a+1):
   
    odd_num = 2 * i - 1
    if i == a:
        print(odd_num, end="")   
    else:
        print(odd_num, end=", ")