#查找文件，模符匹配
#
#
#
#

import os

path = r'F:\MyWork\01_Project\01_Code\04_SOC19A_NewFW\05_FactoryData\POS3.6715\POS3.6715\414'
filename = '102'
result = []

# 将查询结果直接输出
def find_file():
    i = 0
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)
                print('%d %s' % (i, write))
                result.append(write)

# 将查询结果保存在文本文档中
def find_file_and_putin_txt():
    i = 0
    open(r'F:\MyWork\01_Project\01_Code\04_SOC19A_NewFW\02_PyScript\POS367_Motor_Rotate\find_file.txt', mode='w').close()
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)

                file_txt = open(r'F:\MyWork\01_Project\01_Code\04_SOC19A_NewFW\02_PyScript\POS367_Motor_Rotate\find_file.txt', mode='a+')
                file_txt.write('%d %s \n' % (i, write))
                result.append(write)


if __name__ == '__main__':
    find_file()
    find_file_and_putin_txt()


