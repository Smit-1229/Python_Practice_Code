""" Accept temp from user
If temp is more than 100- air
If temp is 0-100 - Water
If temp is less than 0 - cold
"""


temp = float(input("Enter Temperature : "))


if temp > 100 :
    print("Air")
elif temp > 0 and temp <=100 :
    print("water")
else :
    print("cold")
    