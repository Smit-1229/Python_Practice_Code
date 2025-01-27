sum1 = 0
sum2 = 0

for i in range(5):
    num = int(input("Enter Number: "))
    if num % 2 == 0 :
        sum1 += num
    else :
        sum2 += num
print(f"odd sum = {sum2} & even sum = {sum1}" )