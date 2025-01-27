dict = {}                               #blank Dict

menu = """
                                    Choose from the Following : 
                                    1 - Add More Product
                                    2 - View Full Menu Of Product
                                    9 - Exit   
                                    """
print(menu)
flag = True

while flag : 
    ask = int(input("Enter from the menu : "))
    if ask == 1:
    #Add Product Item 
        status = True
        while status :
            #Sub Dict is created for store of price & Quantity of product
            sub_dict = {} 

            #Product Name, price & Quantity Is Taken From User                                                             
            product = input("Enter Statnaiory Product Name : ").capitalize()                        
            price = int(input("Enter Price of Product : " ))                          
            quantity = int(input("Enter Quantity : "))                                
            print()
            #Price & Quantity  is store in dict
            sub_dict["price"] = price                                                  
            sub_dict["Quantity" ] = quantity                                           
            
            #product value is store in main dict
            dict[product] = sub_dict                                                  
            
            print(dict)
            #Loop Repeating 
            choice = input("If You Want To Enter More Product Press 'y' For Yes And 'n' for No : ").lower()
            
            if choice == "n" or choice == "no":
                break
            print()
    
    elif ask == 2 :
    #Show Full Menu
        print(dict)

    elif ask == 9 :
        break
    else:
        print("Invalid Input")









