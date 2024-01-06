city_dict={
    'rasht':'013',
    'hamedan':'081',
    'shiraz':'071',
    'bojnourd':'058'
}

print("city code :2 / city name:1")
select_user=input("enter:")

if select_user == "1" or select_user == "city name":
    search_box=input("enter city name:")
    if search_box in city_dict:
        print("the code is:"+city_dict[search_box])
    
elif select_user == "2" or select_user == "city code":
    search_box=input("enter city code:")
    for k,v in city_dict.items():
        if search_box == v :
            print("the name is:"+k)
