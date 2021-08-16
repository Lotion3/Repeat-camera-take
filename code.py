from cv2 import cv2
import numpy
import random
import time

clock=time.time()
amount=10

def take_picture():
    videocapture=cv2.VideoCapture(0) 
    result=True
    amount=random.randint(1,11)
    while(result):
        ret,frame=videocapture.read()
        cv2.imwrite("picture" + str(amount) + ".jpg",frame)
        clock=time.time
        result=False
    
    videocapture.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time()-clock)>=5 & amount>0):
            take_picture()
            amount-1
            print(amount)

main()