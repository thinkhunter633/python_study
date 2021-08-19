'''
This project simulate random supply temprature
'''

#Import Library
import csv
#from typing import ClassVar
from BACBase import *
# from ede357 import *
import random
# from basic_service import *

if __name__ == '__main__':
    while True:
        i=i+1
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("LoopIndex:" + str(i) + "Time:" + str(now))
        # 1st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,5)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 2nd minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,20)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 3rd minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,50)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 4st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,75)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 5st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 6st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,50)
        time.sleep(60)
        # 7st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,100)
        time.sleep(60)
        # 8st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,100)
        time.sleep(60)
        # 9st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,100)
        time.sleep(60)
        # 10st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,75)
        time.sleep(60)
        # 11st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,35)
        time.sleep(60)
        # 12st minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,100)
        bacWrite(HclElPos,0)
        time.sleep(60)
         # 13t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,80)
        bacWrite(HclElPos,0)
        time.sleep(60)
         # 14t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,60)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 15t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,30)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 16t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,10)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 17t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,5)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 18t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,3)
        bacWrite(HclElPos,0)
        time.sleep(60)
        # 19t minute
        bacWrite(FanSuSpd,75)
        bacWrite(FanEhSpd,75)
        bacWrite(RotHExgSpd,0)
        bacWrite(HclElPos,0)
        time.sleep(60)
         # 20~25 minute
        bacWrite(FanSuSpd,50)
        bacWrite(FanEhSpd,50)
        bacWrite(RotHExgSpd,0)
        bacWrite(HclElPos,0)
        time.sleep(60*5)
        # 25~30 minute
        bacWrite(FanSuSpd,25)
        bacWrite(FanEhSpd,25)
        bacWrite(RotHExgSpd,0)
        bacWrite(HclElPos,0)
        time.sleep(60*5)





    # i=0
    # while True:
    #     # warmstart("192.168.1.102", "")
    #     i=i+1
    #     print("LoopIndex:" + str(i))
    #     # bacWrite(RotHExgSpd,3)
    #     bacWrite(RotHExgSpd,5)
    #     time.sleep(90)
    #     RotCur = bacRead(RotHExgCur)
    #     print("CoilCurrent  " + str(RotCur))
    #     if RotCur == 0:
    #         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         print(now)
    #         break
    #     else:
    #         bacWrite(RotHExgSpd,0)
    #         time.sleep(30)

