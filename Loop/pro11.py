#Accept 5 marks and if above 70 a grade and below 70 is b grade
 

for i in range(6):
    marks = int(input("Enter Marks : "))
    if marks < 100 and marks > 0 :
        if marks > 70 :
            print("A grade")
        else :
            print("B grade")
    else :
        print("marks are invalid")
