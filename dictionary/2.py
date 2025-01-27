#blank Dict
dict = {}                               

menu = """
                                    Choose from the Following : 
                                    1 - Add More Product
                                    2 - View Full Menu Of Product
                                    3 - View Specific Product 
                                    9 - Exit   
                                    """

flag = True

while flag : 
    print(menu)
    ask = int(input("Enter from the menu : "))
    print()
    if ask == 1:
    #Add Product Item 
        status = True
        while status :
            #Sub Dict is created for store of price & Quantity of product
            sub_dict = {} 

            #Product Name, price & Quantity Is Taken From User                                                             
            product = input("Enter Statnaiory Product Name : ").capitalize()                        
            price = int(input("Enter Price of Product : " ))                          
            quantity = int(input("Enter Minimum Quantity : "))                                
            print()
            #Price & Quantity  is store in dict
            sub_dict["price"] = price                                                  
            sub_dict["Quantity" ] = quantity                                           
            
            #product value is store in main dict
            dict[product] = sub_dict                                                  
            
            print(dict)
            
            print()
            #Loop Repeating 
            choice = input("If You Want To Enter More Product Press 'y' For Yes And 'n' for No : ").lower()
            
            if choice == "n" or choice == "no":
                print()
                break
            print()
    
    elif ask == 2 :
    #Show Full Menu
        print("Here Are The Following Product And Quantity : ")
        for i in dict:
            print(i, end=" :")
            print()
            print(f"Price : {dict[i]["price"]}",end=", ")
            print(f"Minimum Quantity : {dict[i]["Quantity"]}")

    elif ask == 3 :
    #Show Specific detail of the product 
        ask_product = input("Enter Porduct : ")

        if ask_product.capitalize() in dict :
            print(dict[ask_product.capitalize()])
        else :
            print("Invalid Product")
    #Break or stop the loop
    elif ask == 9 :
        break

    #Input not in the menu
    else :
        print("Invalid Input")










