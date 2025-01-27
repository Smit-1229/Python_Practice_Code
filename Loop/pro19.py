#prime number

num = int(input("Enter a number : "))
flag = True
for i in range(2,num):
    if num%i == 0:
        flag = False
        break
    else :
        flag = True
if flag:
    print("prime num")
else :
    print("Not a prime num")