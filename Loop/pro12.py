# accept5 mark and do add of above 70 marks

sum = 0
for i in range(5):
    mark = int(input("Enter marks : "))
    if mark > 70 :
        sum += mark
print(f"Total Marks = {sum}")