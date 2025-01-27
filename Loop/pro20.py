#strong number
for p in range(1,100000000000001):
    num = p 

    temp = num

    sum = 0
    while num!=0:
        rem = num%10
        fact = 1
        for i in range(1,rem+1):
            fact *= i

        sum += fact
        num = num//10

    if sum == temp :
        print(f"{temp} is strong number")
    



