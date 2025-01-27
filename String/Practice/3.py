"""
Count Vowels and Consonants
Write a function to count the number of vowels and consonants in a string.
Example: "hello" → Vowels: 2, Consonants: 3
"""

string = input("Enter Word : ")

count_vowel = 0
count_consonants = 0
vowel = {"a","e","i","o","u"}
for c in string:
    if len(c) == 1 and string.isalpha():
        if c.lower() in vowel :
            count_vowel+=1
        else:
            count_consonants+=1
    else:
        print("Enter a valid input for check")

print(f"The Vowel in \'{string}\' are {count_vowel} & consonants are {count_consonants}")