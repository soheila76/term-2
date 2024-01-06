books=['old man and the sea','lord of the flies','empty world','harry potter']
print(f"Books in our library: {books}")
UserBook=input("select a book of list: ")
if UserBook != "":
    if UserBook == "old man and the sea":
        print("Ernest Hemingway")
        
    elif UserBook == "lord of the flies":
        print("William Golding")
        
    elif UserBook == "empty world":
        print("John Christopher")
        
    elif UserBook == "harry potter":
        print("J. K. Rowling")
    
else:
    print("The input is empty!!")