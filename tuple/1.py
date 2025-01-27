tuple_1 = ("Smit","Vishwa",50,60)                               #Create a tuple


tuple_1 = tuple_1 + ("yuvraj",)                                  #way to add element in tuple


tuple_1 = tuple_1[:2] + ("kishan",) +tuple_1[3::-1]              #way to add element at specific location


list_1 = list(tuple_1)                                           #Anotther way for adding element
list_1.append("isha")
tuple_1 = tuple(list_1)



print(tuple_1)

