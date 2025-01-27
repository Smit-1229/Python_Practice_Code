#Armstrong number
for i in range(1,10001):
    num=i
    temp=num
    sum=0
    while num!=0 :
        cube = 1
        rem = num % 10
        cube = rem**3

        sum += cube
        num = num//10

    if sum == temp :
        print(f"{temp} is armstrong number")

    else:
        pass



