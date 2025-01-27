"""Accept years from user and convert into months

eg. year = 1
month = 12
"""

year = int(input("Enter no. of years : "))

if year >= 0:
    month = year*12
    print(f"month = {month}")
else :
    print("invalid year")



