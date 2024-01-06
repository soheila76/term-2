#ذخیره در فایل تا وقتی که کاربر بخواهد
cf=open("contact.txt","a")
while True:
    name=input("First Name:  ")
    if name == "end":
        break
    lname=input("Last Name:  ")
    phone_number=input("enter phone number:  ")
    cf.write(f"First name:{name}\nLast name: {lname}\nPhone number: {phone_number}\n")
    cf.write("*******************************\n")

        