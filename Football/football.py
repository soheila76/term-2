import random
print("Hi,welcome..")
print("⚽️This is a football app for football fans⚽️")
like=input("do you like football?  yes/no:")

if like == "yes":
    print("it's good..")
    print("let's go to test⚽️⚽️⚽️")
    q_list=['which team was the champion of the 2022 World Cup?',
            'which team was the champion of the Europe champions league?',
            "who won the Ballon d'Or 2022?",
            'How many teams participated in the 2022 World Cup?',
          ]
    pc_select=random.choice(q_list)
    print(pc_select)
    user_answer=input(":")
    if pc_select == q_list[0] :
        if user_answer == "Argentina":
            print("it's true / you win")
        else:
            print("it's false / you lose")
    elif pc_select == q_list[1]:
        if user_answer == "Real madrid":
            print("it's true / you win")
        else:
            print("it's false / you lose")
    elif pc_select == q_list[2]:
        if user_answer == "karim benzema":
            print("it's true / you win")
        else:
            print("it's false / you lose")
    elif pc_select == q_list[3]:
        if user_answer == "32":
            print("it's true/ you win")
        else:
            print("it's false / you lose")
    elif pc_select == q_list[4]:
        pass
    elif pc_select == q_list[5]:
        pass
    elif pc_select == q_list[6]:
        pass
    elif pc_select == q_list[7]:
        pass
    
elif like == "no":
    print("goodbye!!! ✋🏿")
else:
    print("you'r answer have a problem!!")
    
