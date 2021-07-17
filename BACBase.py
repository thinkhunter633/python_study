"""This programme is based on MIchael def function
and self define function to test POS3.5715 BACnet
Auhor : Messi
Date : 20200826
Version : 1.1.0
"""

import time

import BAC0
from ede_AS70 import *
#from ede357 import *

# Test initdata define
# adapter_ip = '192.168.1.109/24'  # outgoing BACnet adapter of this PC /24 means subnet mask 255.255.255.0
adapter_ip = '192.168.31.105/24'   #run python pc

# create a logfile
def createlog(filepath, testname):
    try:
        f = open(filepath, "w")
        f.write(f"{testname} " + "\n")
        f.close()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        f = open(filepath, "a")
        f.write(f"Test started Time : {current_time} \n")
        f.close()
        print("Test init data write successful")
    except:
        print("Write test log init information failed")


# define write log method
def writeLog(stepno, steptxt, passed):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if passed:
        restxt = "passed"
    else:
        restxt = "failed"
    dsptext = current_time + " Step " + stepno + ": " + steptxt + " --> " + restxt
    print(dsptext)
    f = open("C:\\TestLog\\POS3.5715_2575\\PyTest.log", "a")
    f.write(dsptext + '\n')
    f.close()


# LiJin Created
def writeLogPer(logtext):
    # self.logtext = logtext
    f = open("C:\\TestLog\\POS3.5715_2575\\PyTest.log", "a")
    f.write(logtext + '\n')
    f.close()


# define name string getting method
def namestr(obj, namespace):
    # gives out a name of the object. Looks for the first objectname that has the value of "obj"
    return [name for name in namespace if namespace[name] is obj]


# define BACnet write method
def bacWrite(obj, val, prop="presentValue", prio="1", printInfo=True):
    # Write object via BACnet
    # args: address objecttype objectindex property value index ("-" when none) priority
    # handling of binary objects, presentValue can be given as is 0 / 1 or as "active" / "inactive"
    objAddr = obj.split()
    objType = objAddr[1]
    try:
        if (
                objType == "binaryInput" or objType == "binaryOutput" or objType == "binaryValue") and prop == "presentValue":
            if str(val) == "1":
                bacnet.write(obj + ' ' + prop + ' ' + "active" + " - " + str(prio))
            elif str(val) == "0":
                bacnet.write(obj + ' ' + prop + ' ' + "inactive" + " - " + str(prio))
        else:
            bacnet.write(obj + ' ' + prop + ' ' + str(val) + " - " + str(prio))
    except:
        hugo = namestr(obj, globals())
        print('ERROR: Bacnet write ' + hugo[0] + ' = ' + str(val))
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: write ' + hugo[0] + ' = ' + str(val))
    return

def bacWritePrio(obj, val, prop="presentValue", prio="2", printInfo=True):
    # Write object via BACnet
    # args: address objecttype objectindex property value index ("-" when none) priority
    # handling of binary objects, presentValue can be given as is 0 / 1 or as "active" / "inactive"
    objAddr = obj.split()
    objType = objAddr[1]
    try:
        if (
                objType == "binaryInput" or objType == "binaryOutput" or objType == "binaryValue") and prop == "presentValue":
            if str(val) == "1":
                bacnet.write(obj + ' ' + prop + ' ' + "active" + " - " + str(prio))
            elif str(val) == "0":
                bacnet.write(obj + ' ' + prop + ' ' + "inactive" + " - " + str(prio))
        else:
            bacnet.write(obj + ' ' + prop + ' ' + str(val) + " - " + str(prio))
    except:
        hugo = namestr(obj, globals())
        print('ERROR: Bacnet write ' + hugo[0] + ' = ' + str(val))
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: write ' + hugo[0] + ' = ' + str(val))
    return


def bacWriteprop(obj, prop, val, printInfo=True):
    # Write object via BACnet
    # args: address objecttype objectindex property value index ("-" when none) priority
    # handling of binary objects, presentValue can be given as is 0 / 1 or as "active" / "inactive"
    # objAddr = obj.split()
    # objType = objAddr[1]
    try:
        bacnet.write(obj + ' ' + prop + ' ' + str(val))
    except:
        hugo = namestr(obj, globals())
        print('ERROR: Bacnet write ' + hugo[0] + ' = ' + str(val))
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: write ' + hugo[0] + ' = ' + str(val))
    return

def bacNorObj(obj, printInfo = True):
    try:
        bacnet.write(obj + ' ' + "outOfService" + ' ' + "true")
        bacnet.write(obj + ' ' + "reliability" + ' ' + "noFaultDetected")
    except:
        hugo = namestr(obj, globals())
        print('ERROR: Bacnet write ' + hugo[0] + ' = ' + 'OOS')
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: write ' + hugo[0] + ' = ' + 'OOS')
    

def bacSimIn(obj, val):
    # Simulate (input) object bia BACnet
    # sets object to out-of service, sets reliability to 0, and writes the value to presentValue
    # object = ip-address + objecttype + instance
    # open: better handling of binary objects, should be 0 / 1 instead of "active" / "inactive"
    try:
        bacnet.write(obj + ' ' + "outOfService" + ' ' + "true")
        bacnet.write(obj + ' ' + "reliability" + ' ' + "noFaultDetected")
        bacWrite(obj, val)
    except:
        hugo = namestr(obj, globals())
        print("ERROR: BACnet simulate " + hugo[0] + ' = ' + str(val))
    return


def bacRead(obj, prop="presentValue", printInfo=False):
    # read object via BACnet
    # handling of binary objects, result is 0 / 1 instead of "active" / "inactive"
    try:
        temp = bacnet.read(obj + " " + prop)
    except:
        hugo = namestr(obj, globals())
        print("ERROR: BACnet read " + hugo[0])
        return ("ERROR")
    else:
        if printInfo:
            hugo = namestr(obj, globals())
            print('Log: read ' + hugo[0] + ' = ' + str(temp))
        objAddr = obj.split()
        objType = objAddr[1]
        if objType == "binaryInput" or objType == "binaryOutput" or objType == "binaryValue":
            if temp == "inactive":
                return (0)
            elif temp == "active":
                return (1)
            else:
                return (temp)
        else:
            return (temp)


# LiJin Create
def bacReadProp(obj, prop, printInfo=False):
    # read object via BACnet
    # handling of binary objects, result is 0 / 1 instead of "active" / "inactive"
    try:
        temp = bacnet.read(obj + " " + prop)
    except:
        hugo = namestr(obj, globals())
        print("ERROR: BACnet read " + hugo[0])
        return ("ERROR")
    else:
        if printInfo:
            hugo = namestr(obj, globals())
            print('Log: read ' + hugo[0] + ' = ' + str(temp))
        objAddr = obj.split()
        objType = objAddr[1]
        if objType == "binaryInput" or objType == "binaryOutput" or objType == "binaryValue":
            if temp == "inactive":
                return (0)
            elif temp == "active":
                return (1)
            else:
                return (temp)
        else:
            return (temp)


def bacCheck(obj, minval, maxval, prop="presentValue", printInfo=True):
    # check, if a BACnet value is between Min and Max. Then result = true
    temp = bacRead(obj, prop)
    if str(temp) == "ERROR":
        result = False
    else:
        if temp < minval or temp > maxval:
            result = False
        else:
            result = True
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: check ' + hugo[0] + ' = ' + str(temp), " Min = ", str(minval), " Max = " + str(maxval))
    return result


# LiJin Create
def bacCheckprop(obj, minval, maxval, prop, printInfo=True):
    # check, if a BACnet value is between Min and Max. Then result = true
    result = True
    temp = bacReadProp(obj, prop)
    if str(temp) == "ERROR":
        result = False
    else:
        if temp < minval or temp > maxval:
            result = False
        else:
            result = True
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: check ' + hugo[0] + ' = ' + str(temp), " Min = ", str(minval), " Max = " + str(maxval))
    return (result)


def bacWait(obj, minval, maxval, Timeout=30, prop="presentValue", printInfo=True):
    # wait until BACnet value is between Min and Max, but at most until timeout is passed
    starttime = time.monotonic()
    askresult = False
    askresult = bacCheck(obj, minval, maxval, prop, False)

    if printInfo:
        print("Log: wait, max " + str(Timeout) + " sec")
    while (time.monotonic() < starttime + Timeout) and not askresult:
        time.sleep(3)
        askresult = bacCheck(obj, minval, maxval, prop, False)
    if printInfo:
        hugo = namestr(obj, globals())
        print('Log: check ' + hugo[0] + ' = ' + str(bacRead(obj, prop)), " Min = ", str(minval),
              " Max = " + str(maxval))
    if askresult:
        return (True)
    else:
        return (False)


######################################################################################################

bacnet = BAC0.connect(ip=adapter_ip)
# bacWrite(ede357.CmfBtn, 1)  # Set to present
# bacWrite(ede357.ROpMod, "null", "presentValue", 13)  # Automatic
