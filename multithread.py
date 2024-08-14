import random
import threading
import email
from threading import Thread
from send_read_email import EMAIL

class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
            
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def showInfo(profile):
    print("Profile: {}\n".format(profile))

def test1(k):
    k = k + 1
    return True
# if __name__ =="__main__":
#     while True:
# p2 = CustomThread(target=test1, args=(1,))
        
# p2.start()
# p1 = CustomThread(target=showInfo, args=(p2.join(),))
# p1.start()
# #         if p1.is_alive():
# #             print("hi")
# #             break
# #         # print(p1.join())   
# #         # print(p2.join())    


# # Check if the thread is alive (running)
# if p1.is_alive():
#     print("Thread is still running")
# else:
#     print("Thread has finished")

# # Wait for the thread to finish (optional)
# p1.join()

# # Check again after the thread has finished
# if p1.is_alive():
#     print("Thread is still running")
# else:
#     print("Thread has finished")