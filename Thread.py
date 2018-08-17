
import threading
def do_this():
    global terminate
    x=0
    print("this is our thread")
    while(terminate==False):
        x+=1
        pass
    print(x)

global terminate
terminate=False
our_thread=threading.Thread(target=do_this)
our_thread.start()
input("hit to stop")
terminate=True


import os
os.system('pause')



