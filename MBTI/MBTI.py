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

    question_number=87
    answer_list=[]
    score=[]
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
        answer=int(input("Lotfan ba 1/2 javab bedeh "))
        if answer == 1 or answer ==2 :
            answer_list.append(answer)
        else:
            answer=int(input("you make a mistake,but you have another chance!please enter 1/2"))
            if answer == 1 or answer ==2 :
                answer_list.append(answer)
            else:
                break


    #part : answer check

    #question 0 : E , I 
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
        scoreI+=0
    elif answer_list[3] == 2:
        scoreE+=1

    #question 4
    if answer_list[4] == 1 :
        scoreI+=1
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
        scoreI+=1
    elif answer_list[7] == 2:
        scoreE+=0

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

    #question 19
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

    if scoreE > scoreI :
        score.append("E")
    elif scoreI > scoreE :
        score.append("I")
    elif scoreI == scoreE :
        score.append("I")

    #question 25 for part 2 : S , N
    if answer_list[25] == 1 :
        scoreS+=1
    elif answer_list[25] == 2:
        scoreN+=1

    #question 26 
    if answer_list[26] == 1 :
        scoreN+=1
    elif answer_list[26] == 2:
        scoreS+=1

    #question 27
    if answer_list[27] == 1 :
        scoreS+=2
    elif answer_list[27] == 2:
        scoreN+=2

    #question 28
    if answer_list[28] == 1 :
        scoreN+=2
    elif answer_list[28] == 2:
        scoreS+=2

    #question 29
    if answer_list[29] == 1 :
        scoreS+=2
    elif answer_list[29] == 2:
        scoreN+=1

    #question 30
    if answer_list[30] == 1 :
        scoreN+=1
    elif answer_list[30] == 2:
        scoreS+=2

    #question 31
    if answer_list[31] == 1 :
        scoreS+=2
    elif answer_list[31] == 2:
        scoreN+=1

    #question 32
    if answer_list[32] == 1 :
        scoreS+=2
    elif answer_list[32] == 2:
        scoreN+=1

    #question 33
    if answer_list[33] == 1 :
        scoreS+=2
    elif answer_list[33] == 2:
        scoreN+=2

    #question 34
    if answer_list[34] == 1 :
        scoreS+=1
    elif answer_list[34] == 2:
        scoreN+=1

    #question 35
    if answer_list[35] == 1 :
        scoreS+=2
    elif answer_list[35] == 2:
        scoreN+=2

    #question 36
    if answer_list[36] == 1 :
        scoreS+=1
    elif answer_list[36] == 2:
        scoreN+=1

    #question 37
    if answer_list[37] == 1 :
        scoreS+=1
    elif answer_list[37] == 2:
        scoreN+=1

    #question 38
    if answer_list[38] == 1 :
        scoreS+=0
    elif answer_list[38] == 2:
        scoreN+=2

    #question 39
    if answer_list[39] == 1 :
        scoreS+=2
    elif answer_list[39] == 2:
        scoreN+=1

    #question 40
    if answer_list[40] == 1 :
        scoreS+=0
    elif answer_list[40] == 2:
        scoreN+=2
    
    #question 41
    if answer_list[41] == 1 :
        scoreN+=1
    elif answer_list[41] == 2:
        scoreS+=0

    #question 42
    if answer_list[42] == 1 :
        scoreN+=1
    elif answer_list[42] == 2:
        scoreS+=2

    #question 43
    if answer_list[43] == 1 :
        scoreN+=2
    elif answer_list[43] == 2:
        scoreS+=2
        
    if scoreN > scoreS :
        score.append("N")
    elif scoreI > scoreE :
        score.append("S")
    elif scoreN == scoreI:
        score.append("N")


    #question 44 for part 3 : T , F
    if answer_list[44] == 1 :
        scoreT+=1
    elif answer_list[44] == 2:
        scoreF+=0

    #question 45
    if answer_list[45] == 1 :
        scoreF+=1
    elif answer_list[45] == 2:
        scoreT+=2

    #question 46
    if answer_list[46] == 1 :
        scoreF+=1
    elif answer_list[46] == 2:
        scoreT+=1

    #question 47 
    if answer_list[47] == 1 :
        scoreF+=0
    elif answer_list[47] == 2:
        scoreT+=1

    #question 48
    if answer_list[48] == 1 :
        scoreF+=1
    elif answer_list[48] == 2:
        scoreT+=0

    #question 49
    if answer_list[49] == 1 :
        scoreF+=1
    elif answer_list[49] == 2:
        scoreT+=0

    #question 50 
    if answer_list[50] == 1 :
        scoreT+=1
    elif answer_list[50] == 2:
        scoreF+=0

    #question 51 
    if answer_list[51] == 1 :
        scoreT+=1
    elif answer_list[51] == 2:
        scoreF+=2

    #question 52 
    if answer_list[52] == 1 :
        scoreF+=2
    elif answer_list[52] == 2:
        scoreT+=2

    #question 53 
    if answer_list[53] == 1 :
        scoreT+=2
    elif answer_list[53] == 2:
        scoreF+=2

    #question 54 
    if answer_list[54] == 1 :
       scoreF+=1
    elif answer_list[54] == 2:
       scoreT+=1

    #question 55 
    if answer_list[55] == 1 :
        scoreT+=1
    elif answer_list[55] == 2:
        scoreF+=1

    #question 56
    if answer_list[56] == 1 :
        scoreT+=2
    elif answer_list[56] == 2:
        scoreF+=2
    
    #question 57 
    if answer_list[57] == 1 :
        scoreT+=0
    elif answer_list[57] == 2:
        scoreF+=2

    #question 58 
    if answer_list[58] == 1 :
        scoreT+=2
    elif answer_list[58] == 2:
        scoreF+=0

    #question 59 
    if answer_list[59] == 1 :
        scoreF+=0
    elif answer_list[59] == 2:
        scoreT+=1

    #question 60 
    if answer_list[60] == 1 :
        scoreT+=2
    elif answer_list[60] == 2:
        scoreF+=0

    #question 61 
    if answer_list[61] == 1 :
        scoreF+=1
    elif answer_list[61] == 2:
        scoreT+=2

    #question 62 
    if answer_list[62] == 1 :
        scoreT+=0
    elif answer_list[62] == 2:
        scoreF+=2

    #question 63 
    if answer_list[63] == 1 :
        scoreF+=1
    elif answer_list[63] == 2:
        scoreT+=1

    #question 64 
    if answer_list[64] == 1 :
        scoreT+=2
    elif answer_list[64] == 2:
        scoreF+=2

    #question 65 
    if answer_list[65] == 1 :
        scoreF+=1
    elif answer_list[65] == 2:
        scoreT+=2

    #question 66 
    if answer_list[66] == 1 :
        scoreF+=0
    elif answer_list[66] == 2:
        scoreT+=2

    #question 67
    if answer_list[67] == 1 :
        scoreF+=0
    elif answer_list[67] == 2:
        scoreT+=2

        
    if scoreT > scoreF :
        score.append("T")
    elif scoreF > scoreT :
        score.append("F")
    elif scoreT == scoreF:
        score.append("F")

    #question 68  for  part 4 :J , P
    if answer_list[68] == 1 :
        scoreJ+=0
    elif answer_list[68] == 2:
        scoreP+=2

    #question 69 
    if answer_list[69] == 1 :
        scoreJ+=1
    elif answer_list[69] == 2:
        scoreP+=1

    #question 70 
    if answer_list[70] == 1 :
        scoreJ+=2
    elif answer_list[70] == 2:
        scoreP+=2

    #question 71 
    if answer_list[71] == 1 :
        scoreJ+=1
    elif answer_list[71] == 2:
        scoreP+=2

    #question 72 
    if answer_list[72] == 1 :
        scoreJ+=1
    elif answer_list[72] == 2:
        scoreP+=2

    #question 73 
    if answer_list[73] == 1 :
        scoreJ+=2
    elif answer_list[73] == 2:
        scoreP+=2

    #question 74 
    if answer_list[74] == 1 :
        scoreP+=2
    elif answer_list[74] == 2:
        scoreJ+=2

    #question 75 
    if answer_list[75] == 1 :
        scoreJ+=1
    elif answer_list[75] == 2:
        scoreP+=2

    #question 76 
    if answer_list[76] == 1 :
        scoreJ+=2
    elif answer_list[76] == 2:
        scoreP+=2

    #question 77 
    if answer_list[77] == 1 :
        scoreP+=1
    elif answer_list[77] == 2:
        scoreJ+=1

    #question 78
    if answer_list[78] == 1 :
        scoreJ+=2
    elif answer_list[78] == 2:
        scoreP+=1

    #question 79 
    if answer_list[79] == 1 :
        scoreJ+=1
    elif answer_list[79] == 2:
        scoreP+=2

    #question 80 
    if answer_list[80] == 1 :
        scoreJ+=2
    elif answer_list[80] == 2:
        scoreP+=0

    #question 81 
    if answer_list[81] == 1 :
        scoreJ+=2
    elif answer_list[81] == 2:
        scoreP+=1

    #question 82
    if answer_list[82] == 1 :
        scoreJ+=2
    elif answer_list[82] == 2:
        scoreP+=2

    #question 83 
    if answer_list[83] == 1 :
        scoreJ+=2
    elif answer_list[83] == 2:
        scoreP+=2

    #question 84 
    if answer_list[84] == 1 :
        scoreJ+=2
    elif answer_list[84] == 2:
        scoreP+=2

    #question 85 
    if answer_list[85] == 1 :
        scoreJ+=1
    elif answer_list[85] == 2:
        scoreP+=1

    #question 86 
    if answer_list[86] == 1 :
        scoreJ+=1
    elif answer_list[86] == 2:
        scoreP+=2

       
    if scoreJ > scoreP :
       score.append("J")
    elif scoreP > scoreJ :
       score.append("P")
    elif scoreJ == scoreP:
        score.append("P")

    print(score)




elif Y_or_N == "n" or Y_or_N == "N":
    print("OK..you can come here for the test in other time!")
else:
    print("your answer must be y/n!")
