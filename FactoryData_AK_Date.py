'''
This programme is for analysising factory data, activation key and manufactorure date mapping
'''

#Import Library
import os
import csv
import time
import random
import shutil
g_Idx = 0
g_TotalFolds = 1
SPLIT_FOLD_NUMBER = 200
g_TotalSplitFold_New = 1
list_foldName = []
CSV_FILE_NAME = "Activation key and manufacture date.csv"


def Init_Create_CSV_File():
    f = open(CSV_FILE_NAME, 'w+', newline='', encoding='utf-8')
    csv_writer =  csv.writer(f)
    csv_writer.writerow(["Index","Activation key", "manufacture date","filename"])
    f.close()
def Write_CSV_File(row):
    f = open(CSV_FILE_NAME, 'a+', newline='', encoding='utf-8')
    csv_writer =  csv.writer(f)
    csv_writer.writerow(row)
    f.close()


# Read Activation key from txt file
def Read_ActivationKeyFromTxt(filenpathame,file_modify_date):
    global g_Idx
    filetxt = open(filenpathame,'r')
    lines = filetxt.readlines()
    tmpStr = lines[0]
    if len(tmpStr) > 10:
        splitresult = tmpStr[0:30]
        g_Idx = g_Idx + 1
        Write_CSV_File([g_Idx,splitresult,file_modify_date,filenpathame])

    filetxt.close()

def walkFile_File(Fold):
    for root, dirs, files in os.walk(Fold):
        for f in files:
            print(os.path.join(root, f))
            if f == "activationkey.txt":
                full_path_name = os.path.join(root, f)
                # print(full_path_name)
                mtime = os.stat(full_path_name).st_mtime
                file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                #print("{0} Modify date: {1}".format(idx_file,file_modify_time))
                # print("{0} Modify date: {1}".format(full_path_name,file_modify_time))
                Read_ActivationKeyFromTxt(full_path_name,file_modify_time)

# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        # idx_file = 0
        # for f in files:
        #     print(os.path.join(root, f))
        #     if f == "activationkey.txt":
        #         full_path_name = os.path.join(root, f)
        #         # print(full_path_name)
        #         idx_file = idx_file + 1
        #         mtime = os.stat(full_path_name).st_mtime
        #         file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        #         #print("{0} Modify date: {1}".format(idx_file,file_modify_time))
        #         # print("{0} Modify date: {1}".format(full_path_name,file_modify_time))
        #         Read_ActivationKeyFromTxt(full_path_name,file_modify_time)

        # 遍历所有的文件夹
        for d in dirs:
            foldname = os.path.join(root, d)
            print(foldname)
            walkFile_File(foldname)

def GetFactoryData_csv(fullfoldname):
    Init_Create_CSV_File()
    walkFile(fullfoldname)

def Create_Parent_Fold(file):
    global g_TotalFolds
    global g_TotalSplitFold_New
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历所有的文件夹
        for d in dirs:
            g_TotalFolds = g_TotalFolds + 1
    print("Fold numbers:{0}".format(g_TotalFolds))

    #create pararent fold
    pararent_fold = "F:/MyWork/01_Project/01_Code/04_SOC19A_NewFW/05_FactoryData/python_SplitFold2/"
    g_TotalSplitFold_New = int(g_TotalFolds/SPLIT_FOLD_NUMBER)
    for foldIdx in range(1,g_TotalSplitFold_New):
        dst_fold = pararent_fold + 'mytest' + str(foldIdx)
        print(dst_fold)
        os.mkdir(dst_fold)
        list_foldName.append(dst_fold)
    print(g_TotalSplitFold_New)

# 遍历文件夹 and move, low performance
# def walkFile_Move(file):
#     # global g_TotalSplitFold_New
#     for splitfoldIndx in range(0,g_TotalSplitFold_New):
#         for root, dirs, files in os.walk(file):
#             # root 表示当前正在访问的文件夹路径
#             # dirs 表示该文件夹下的子目录名list
#             # files 表示该文件夹下的文件list
#             # 遍历所有的文件夹
#             for d in dirs:
#                 myRestVal = int(d)/SPLIT_FOLD_NUMBER
#                 if int(myRestVal) == splitfoldIndx :
#                     dstfullname = "F:/MyWork/01_Project/01_Code/04_SOC19A_NewFW/05_FactoryData/python_SplitFold/mytest" + str(splitfoldIndx + 1) + "/" + str(d)
#                     shutil.copytree(os.path.join(root, d),dstfullname)
#             print("-"*splitfoldIndx)

def walkFile_Move(file):
    # global g_TotalSplitFold_New
        for root, dirs, files in os.walk(file):
            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list
            # 遍历所有的文件夹
            for d in dirs:
                myRestVal = int(d)/SPLIT_FOLD_NUMBER
                for splitfoldIndx in range(0,g_TotalSplitFold_New):
                    if int(myRestVal) == splitfoldIndx :
                        dstfullname = "F:/MyWork/01_Project/01_Code/04_SOC19A_NewFW/05_FactoryData/python_SplitFold2/mytest" + str(splitfoldIndx + 1) + "/" + str(d)
                        shutil.copytree(os.path.join(root, d),dstfullname)
                print("-"*int(myRestVal))

DATABASEFOLD = "F:/MyWork/01_Project/01_Code/04_SOC19A_NewFW/05_FactoryData/output0808/output"
# DATABASEFOLD = "F:/MyWork/01_Project/01_Code/04_SOC19A_NewFW/05_FactoryData/test1"
def main():
    #chenewei ,detele those code for mistake press button
    Create_Parent_Fold(DATABASEFOLD)
    walkFile_Move(DATABASEFOLD)

    # #Analysis every fold
    Init_Create_CSV_File()
    for listindex in list_foldName:
         walkFile(listindex)

    print("---------------Done!-------------------------------------")


if __name__ == '__main__':
    main()

