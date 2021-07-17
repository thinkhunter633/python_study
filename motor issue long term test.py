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

#Project start
# def changetemp(obj, var):
#     bacWrite(obj,var)
#     time.sleep(20)
#     motorval = bacRead(RotHExgSpd)
#     motorcur = bacRead(RotHExgCur)
#     now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     restxt = 'TSu is : ' + str(var) + ' ' + 'Motor Speed is :' + ' ' + str(motorval)+' '+'Motor Current is '+str(motorcur)
#     rescsv = [str(now), str(motorval), str(motorcur)]
#     print(restxt)
#     return rescsv

# def write_csv(row):
#     f =  open('inputfile/MotorMonitor.csv', 'a')
#     f.write('\xEF\xBB\xBF')
#     writer = csv.writer(f)
#     writer.writerow(row)


if __name__ == '__main__':
    # bacWrite(RotHExgSpd,0)
    # time.sleep(5)
    # bacWrite(RotHExgSpd,1)
    # now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(now)
    # i = 0
    # for i in range(1, 14400000, 1):
    #     motorcur = bacRead(RotHExgCur)
    #     if motorcur !=0:
    #         break
    # now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(now)
    # LTdevice_ip = '192.168.50.100' + " "
    # RotHExgSpdNH = LTdevice_ip + 'analogOutput 0'

    
    i=0
    while True:
        # warmstart("192.168.1.102", "")
        i=i+1
        print("LoopIndex:" + str(i))
        # bacWrite(RotHExgSpd,3)
        bacWrite(RotHExgSpd,3)
        time.sleep(90)
        RotCur = bacRead(RotHExgCur)
        print("CoilCurrent" + str(RotCur))
        if RotCur == 0:
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(now)
            break
        else:
            bacWrite(RotHExgSpd,0)
            time.sleep(30)



    

    



