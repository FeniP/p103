import time
#print(dir(time))
seconds=int(input("enter the time in number of seconds:"))
def counter(seconds):
    while seconds>0:
        m=int(seconds/60)
        s=int(seconds%60)
        timer=f'{m}:{s}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print("times up")
counter(seconds)
