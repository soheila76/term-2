#فروشگاه با لیست و ثبت خرید های مشتری در فایل
hardwars=['Mouse','RAM','Monitor','Sound card','Computer memory','Motherboard']
print(hardwars)


user_selection=input("Choose the product you need:  ")
if user_selection in hardwars:
    cf=open("shopping.txt","a")
    
    if user_selection == hardwars[0]:
        cf.write(f"order: \t{user_selection} \n")
        models=["Glorious Gaming","Logitech M510 Wireless ","EVGA X20 Wireless Gaming"," SOLAKAKA SM800","Logitech G402","Superglide2"]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")
            cf.write("**********************************************\n")
            
            
    elif user_selection == hardwars[1]:
        cf.write(f"order: \t{user_selection} \n")
        models=["Corsair VENGEANCE RGB PRO","NVTEK 64GB (2x32GB)","TEAMGROUP T-Force"]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")           
            cf.write("**********************************************\n")
                    
    elif user_selection == hardwars[2]:
        cf.write(f"order: \t{user_selection} \n")
        models=["SAMSUNG 34","ASUS TUF Gaming 32","MSI G27CQ4 E2, 27"]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")            
            cf.write("**********************************************\n")
            
    elif user_selection == hardwars[3]:
        cf.write(f"order: \t{user_selection} \n")
        models=["Sound Blaster Audigy","PHOINIKAS T10 External","PHOINIKAS T10 External"]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")            
            cf.write("**********************************************\n")
                   
    elif user_selection == hardwars[4]:
        cf.write(f"order: \t{user_selection} \n")
        models=["Kingston Server Premier 32 GB","NVTEK 64GB (2x32GB)","TEAMGROUP T-Force Delta RGB "]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")            
            cf.write("**********************************************\n")
            
    elif user_selection == hardwars[4]:
        cf.write(f"order: \t{user_selection} \n")
        models=["Intel Core i7-13700K","AMD Ryzen 5 5600X 6-core:","AMD Ryzen 7 5800X 8-core"]
        print(models)
        user_model=input("choose the model of mouse:")
        if user_model in models:
            print("Added to cart")
            cf.write(f"User request : \t {user_model}\n")            
            cf.write("**********************************************\n")
            
else:
    print("We don't have the product you want")

