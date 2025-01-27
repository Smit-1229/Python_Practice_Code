"""
Check Palindrome
Determine if a given string is a palindrome (reads the same backward as forward).
Example: "racecar" → True
"""

string = input("Enter Word : ").lower()
rev_string = string[::-1]

status = True
if string == rev_string :
    print(f"\"{string.capitalize()}\" → {status}")
else:
    status = False
    print(f"\"{string.capitalize()}\" → {status}")
    