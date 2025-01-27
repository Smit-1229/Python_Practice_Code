product_price = {
    "pen":50 , 
    "pencil": 20,
    "sharpner" : 10,
    "rubber" : 5,
    "scale":15,
      }
print(product_price)
x = product_price.copy()                               #Copy Fun 
product_price.clear()                                  #Clear Fun
print(product_price)
print(x)
print(x.get("pencil"))                                 #Get Function
print(x["pencil"])                                     #other ways for get 
print(x.items())                                       #Print key and value in tuple format
print(x.keys())                                        #print keys of dict
print(x.values())                                      #print all the value in dict
x.pop("pen")                                           #removes the key 
print(x)
x.popitem()                                            #by default it removes the last key
print(x)
x.update({"notebook": 50})                             #it add new key and value and if key is already there it update the value
print(x)
print(x.setdefault("notebook",))                       #it gives the specific value of key and print none if there is no deafult value
print(len(x))                                          #it gives the number of lengeth or no. of key in dict
del product_price                                      #it delete the dict 
print(sorted(x))                                       #it sort the dict in alphabetical order
