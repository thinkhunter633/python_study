'''
This project simulate random supply temprature
'''

#Import Library
import csv
#from typing import ClassVar
from BACBase import *
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
#     f =  open('MotorLog.csv', 'a')
#     f.write('\xEF\xBB\xBF')
#     writer = csv.writer(f)
#     writer.writerow(row)
CSV_FILE_NAME = "MotorLog.csv"
def Write_CSV_File(row):
    f = open(CSV_FILE_NAME, 'a+', newline='', encoding='utf-8')
    csv_writer =  csv.writer(f)
    csv_writer.writerow(row)
    f.close()


def Init_Create_CSV_File():
    f = open(CSV_FILE_NAME, 'w', newline='', encoding='utf-8')
    csv_writer =  csv.writer(f)
    csv_writer.writerow(["TimeStamp", "Speed","CoilCurrent"])
    f.close()

if __name__ == '__main__':
    i=0
    Init_Create_CSV_File()
    while True:
        # warmstart("192.168.1.102", "")
        i=i+1
        print("LoopIndex:" + str(i))
        val = random.randint(1,100)
        bacWrite(RotHExgSpd,val)
        time.sleep(90)
        RotCur = bacRead(RotHExgCur)
        print("Case1: CoilCurrent  " + str(RotCur))
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Write_CSV_File([now,val,RotCur])
        if RotCur == 0:
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("case1 failure:" + now)
            break
        else:
            val2 = random.randint(1,100)
            bacWrite(RotHExgSpd,val2)
            time.sleep(90)
            RotCur2 = bacRead(RotHExgCur)
            print("Case2:CoilCurrent  " + str(RotCur2))
            if RotCur2 == 0:
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print("case2 failure:" + now)
                break
            else:
                bacWrite(RotHExgSpd,0)
                time.sleep(30)









