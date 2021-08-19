'''
This project simulate random supply temprature
'''

#Import Library
import csv
from BACBase import *
import random
# from basic_service import *

def check_MyControllers_RunningTime():
    DevRunTime = bacRead(POS367_DevSysRunTm_Min)
    print("-"*60)
    print("Test Objective: Check controller running time!!!!!!!!!!!!!!!")
    print("Timestamp:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(str(POS367_DevSysRunTm_Min) + '\t'+ " DevRunTime: " + str(DevRunTime) + " Minutes, " + '\t' + str(format(DevRunTime/60/24,'.2f')) + " day")
    # Read POS3.57 controller running time
    DevRunTime = bacRead(POS357_DevSysRunTm_Min)
    print(str(POS357_DevSysRunTm_Min) + '\t'+ " DevRunTime: " + str(DevRunTime) + " Minutes, " + '\t' + str(format(DevRunTime/60/24,'.2f')) + " day")

    POS357_104_DevSysRunTm_Min = '192.168.31.104' + " " + 'analogValue 721'
    DevRunTime = bacRead(POS357_104_DevSysRunTm_Min)
    print(str(POS357_104_DevSysRunTm_Min) + '\t' + " DevRunTime: " + str(DevRunTime) + " Minutes, " + '\t' + str(format(DevRunTime/60/24,'.2f')) + " day")

    POS357_102_DevSysRunTm_Min = '192.168.31.102' + " " + 'analogValue 721'
    DevRunTime = bacRead(POS357_102_DevSysRunTm_Min)
    print(str(POS357_102_DevSysRunTm_Min) + '\t' + " DevRunTime: " + str(DevRunTime) + " Minutes, " + '\t' + str(format(DevRunTime/60/24,'.2f')) + " day")
    print("-"*60)

def check_MyControllers_RUB_PDO_STATE():
    print("Test Objective: Check PDO state!!!!!!!!!!!!!!!")
    POS367_RUB_PDO_State = bacRead(POS367_ROpUn)
    print(str(POS367_ROpUn) + '\t' + " POS367 RUB state: " + str(POS367_RUB_PDO_State))

    POS367_103_RUBPDO_Obj = '192.168.31.103' + " " + 'multiStateValue 331'
    POS367_103_RUBPDO_State = bacRead(POS367_103_RUBPDO_Obj)
    print(str(POS367_103_RUBPDO_Obj) + '\t' + " POS357 RUB state: " + str(POS367_103_RUBPDO_State))

    POS367_104_RUBPDO_Obj = '192.168.31.104' + " " + 'multiStateValue 331'
    POS367_104_RUBPDO_State = bacRead(POS367_104_RUBPDO_Obj)
    print(str(POS367_104_RUBPDO_Obj) + '\t' + " POS357 RUB state: " + str(POS367_104_RUBPDO_State))

    POS367_102_RUBPDO_Obj = '192.168.31.102' + " " + 'multiStateValue 331'
    POS367_102_RUBPDO_State = bacRead(POS367_102_RUBPDO_Obj)
    print(str(POS367_102_RUBPDO_Obj) + '\t' + " POS357 RUB state: " + str(POS367_102_RUBPDO_State))

    print("-"*70)


if __name__ == '__main__':

    # Read POS3.67 controller running time
    check_MyControllers_RunningTime()
    check_MyControllers_RUB_PDO_STATE()

    #Test Objective: Check PDO state
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

