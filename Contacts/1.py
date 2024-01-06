#ذخیره شماره تماس و اطلاعات هر کاربر در فایل
name=input("First Name:  ")
lname=input("Last Name:  ")
phone_number=input("enter phone number:  ")
if name != "" and phone_number != "":
    cf=open("contact.txt","a")
    cf.write(f"First name:{name}\nLast name: {lname}\nPhone number: {phone_number}\n")
    cf.write("*******************************\n")
else:
    print("empty error!!")
