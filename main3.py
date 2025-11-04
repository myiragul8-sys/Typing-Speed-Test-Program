from time import *
import random as r
print(time())
def  mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error +1
        except :
            error=error +1
    return error       
def speed_time(time_s,time_e,userinput): 
    time_delay=time_e-time_s 
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)       
if __name__=='__main__'  :          
    while True:
        ck=input("ready to test:yes/no:")
        if ck=="yes":
            test=["a paragraph is a self continued unit of discourse in writing dealing with a particular point or idea", "my name is guk","i read"]
            test1=r.choice(test)
            print("*****typing speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter the text: ")
            time_2 = time()
            typing_speed = speed_time(time_1, time_2, testinput)
            error_count = mistake(test1, testinput)
            print(f"Typing speed: {typing_speed} w/sec")
            print(f"Errors: {error_count}")
        elif ck=="no":
            print("thank you") 
            break
        else :
            print("wrong input")
      
    