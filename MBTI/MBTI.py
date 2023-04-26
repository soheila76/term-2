from qustions import *
import time
import os

Y_or_N=input("Are you ready for MBTI test?  (y/n)")
if Y_or_N == "y" or Y_or_N == "Y":
    print("Hello,this is a MBTI test and\nIf you make a mistake,you have just 2 chance for each question..")
    print("let's go to the test..")
    time.sleep(1)
    for i in range(3,-1,-1):
        loading=i
        time.sleep(2)
        os.system("clear") #برای اینکه تایمر ما در یک خط نمایش داده بشه
        print(loading)
        time.sleep(0.9)

    question_number=2
    answer_list=[]
    scoreE=0
    scoreI=0
    scoreS=0
    scoreN=0
    scoreT=0
    scoreF=0
    scoreJ=0
    scoreP=0

    for i in range(question_number):
        print(question_tab[i])
        answer=int(input("please answer with 1/2: "))
        if answer == 1 or answer ==2 :
            answer_list.append(answer)
        else:
            answer=int(input("you make a mistake,but you have another chance!please enter 1/2"))
            if answer == 1 or answer ==2 :
                answer_list.append(answer)
            else:
                break
    print(answer_list)

    #part : answer check

    #question 0
    if answer_list[0] == 1 :
        scoreE+=1
    elif answer_list[0] == 2:
        scoreI+=2

    #question 1
    if answer_list[1] == 1 :
        scoreE+=2
    elif answer_list[1] == 2:
        scoreI+=2

    #question 2
    if answer_list[2] == 1 :
        scoreE+=2
    elif answer_list[2] == 2:
        scoreI+=2

    #question 3
    if answer_list[3] == 1 :
        scoreI+=2
    elif answer_list[3] == 2:
        scoreE+=2

    #question 4
    if answer_list[4] == 1 :
        scoreI+=2
    elif answer_list[4] == 2:
        scoreE+=2

    #question 5
    if answer_list[5] == 1 :
        scoreI+=1
    elif answer_list[5] == 2:
        scoreE+=1

    #question 6
    if answer_list[6] == 1 :
        scoreE+=2
    elif answer_list[6] == 2:
        scoreI+=2

    #question 7
    if answer_list[7] == 1 :
        scoreI+=0
    elif answer_list[7] == 2:
        scoreE+=1

    #question 8
    if answer_list[8] == 1 :
        scoreI+=0
    elif answer_list[8] == 2:
        scoreE+=1

    #question 9
    if answer_list[9] == 1 :
        scoreE+=0
    elif answer_list[9] == 2:
        scoreI+=1

    #question 10
    if answer_list[10] == 1 :
        scoreE+=2
    elif answer_list[10] == 2:
        scoreI+=2

    #question 11
    if answer_list[11] == 1 :
        scoreI+=2
    elif answer_list[11] == 2:
        scoreE+=2

    #question 12
    if answer_list[12] == 1 :
        scoreI+=2
    elif answer_list[12] == 2:
        scoreE+=1

    #question 13
    if answer_list[13] == 1 :
        scoreI+=1
    elif answer_list[13] == 2:
        scoreE+=2

    #question 14
    if answer_list[14] == 1 :
        scoreE+=0
    elif answer_list[14] == 2:
        scoreI+=1

    #question 15
    if answer_list[15] == 1 :
        scoreI+=1
    elif answer_list[15] == 2:
        scoreE+=2

    #question 16
    if answer_list[16] == 1 :
        scoreI+=2
    elif answer_list[16] == 2:
        scoreE+=2

    #question 17
    if answer_list[17] == 1 :
        scoreE+=2
    elif answer_list[17] == 2:
        scoreI+=1

    #question 18
    if answer_list[18] == 1 :
        scoreE+=2
    elif answer_list[18] == 2:
        scoreI+=2

    #question 18
    if answer_list[19] == 1 :
        scoreE+=2
    elif answer_list[19] == 2:
        scoreI+=2

    #question 20
    if answer_list[20] == 1 :
        scoreE+=1
    elif answer_list[20] == 2:
        scoreI+=1

    #question 21
    if answer_list[21] == 1 :
        scoreE+=2
    elif answer_list[21] == 2:
        scoreI+=0

    #question 22
    if answer_list[22] == 1 :
        scoreE+=1
    elif answer_list[22] == 2:
        scoreI+=2

    #question 23
    if answer_list[23] == 1 :
        scoreE+=1
    elif answer_list[23] == 2:
        scoreI+=2

    #question 24
    if answer_list[24] == 1 :
        scoreE+=1
    elif answer_list[24] == 2:
        scoreI+=1

    #question 25 for part 2
    if answer_list[25] == 1 :
        scoreE+=1
    elif answer_list[25] == 2:
        scoreI+=1

    #question 26 
    if answer_list[26] == 1 :
        score+=2
    elif answer_list[26] == 2:
        score+=2

    #question 27
    if answer_list[27] == 1 :
        score+=2
    elif answer_list[27] == 2:
        score+=2

    #question 28
    if answer_list[28] == 1 :
        score+=2
    elif answer_list[28] == 2:
        score+=2

    #question 29
    if answer_list[29] == 1 :
        score+=2
    elif answer_list[29] == 2:
        score+=2

    #question 30
    if answer_list[30] == 1 :
        score+=2
    elif answer_list[30] == 2:
        score+=2

    #question 31
    if answer_list[31] == 1 :
        score+=2
    elif answer_list[31] == 2:
        score+=2

    #question 32
    if answer_list[32] == 1 :
        score+=2
    elif answer_list[32] == 2:
        score+=2

    #question 33
    if answer_list[33] == 1 :
        score+=2
    elif answer_list[33] == 2:
        score+=2

    #question 34
    if answer_list[34] == 1 :
        score+=2
    elif answer_list[34] == 2:
        score+=2

    #question 35
    if answer_list[35] == 1 :
        score+=2
    elif answer_list[35] == 2:
        score+=2

    #question 36
    if answer_list[36] == 1 :
        score+=2
    elif answer_list[36] == 2:
        score+=2

    #question 37
    if answer_list[37] == 1 :
        score+=2
    elif answer_list[37] == 2:
        score+=2

    #question 38
    if answer_list[38] == 1 :
        score+=2
    elif answer_list[38] == 2:
        score+=2

    #question 39
    if answer_list[39] == 1 :
        score+=2
    elif answer_list[39] == 2:
        score+=2

    #question 40
    if answer_list[40] == 1 :
        score+=2
    elif answer_list[40] == 2:
        score+=2


    print(score)


elif Y_or_N == "n" or Y_or_N == "N":
    print("OK..you can come here for the test in other time!")
else:
    print("your answer must be y/n!")






