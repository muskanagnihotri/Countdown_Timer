import time 
def countdown(t):
    while t:
        mins,secs=divmod(t,60) #calculate the number of minutes and seconds

        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1) #used to make a code wait for one sec
  
        t-=1
    print('YEAH YEAH FIRE')

t=input("Enter the time in seconds: ")
countdown(int(t))