import random
from time import *
import random as r

def mistake(paragraph,userinput):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != userinput[i]:
                error = error +1
        except Exception as e :
            error = error +1
    return error

def spped_time(time_start,time_end,userinput):
    time_delay = time_end - time_start
    time_r = round(time_delay,2)
    spped = len(userinput)/time_r
    return round(spped)


test = ["A paragraph which you will be type again and again","welcome to my web_page and now your turn please say what are doing","hlo guys this is not easy for all"]

test1 = random.choice(test)
print("******** typing Speed **********")
print(test1)
print()
print()
time_1 = time()
your_turn = input("Enter your turn:--")
time_2 = time()

print('speed :--',spped_time(time_1,time_2,your_turn),"w/sec")
print("Error:--",mistake(test1,your_turn))

