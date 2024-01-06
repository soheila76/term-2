#فروشگاه با لیست و قرعه کشی مجموع خرید ها
import random

hardwars=['Mouse','RAM','Monitor','Sound card','Computer memory','Motherboard']
print(hardwars)

shopping_list=[]
for i in  range (3):
    user_selection=input("Choose the product you need:  ")
    shopping_list.append(user_selection)

Lottery=random.choices(shopping_list)
print(f"lottery winner : {Lottery} ")