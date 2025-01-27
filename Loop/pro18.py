# find factorial value

f = 1
num = int(input("Enter a num : "))

for i in range(1,num+1):
    f*=i

print(f"The factorial value of {num} is {f}")