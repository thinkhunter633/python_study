import time
import datetime
import MyDbUtil
import copy
import os
import csv
import re
# import ReadWrite
class MotorTest(object):

    def __init__(self):
        self.mysql_info = {"host": '192.168.31.100',
                      "port": 3306,
                      "user": 'soc_user',
                      "password": '123456',
                      "charset": 'utf8'}
        # self.Obj_type = [48, 48, 1]
        # self.Obj_Ins = [400, 404, 0]
        # self.Obj_Property = [85, 85, 85]
        # self.Obj_name = ['coilCul', 'PrSpeed', 'RotHeat']
        # self.DevKey = "PH1234455555"
        # self.deviceIP = "192.168.31.102"
        # self.pcip = "192.168.31.100"
        self.dic_data = {}
        self.dic_cloudinventorylist = []
        # self.dev_error = {}
        # self.cnt = 1
        # self.tt = ReadWrite.ReadWrite()
        # self.bb = self.tt.build_bacnet_connection(self.pcip)
        self.mydb = MyDbUtil.MyDbUtil(self.mysql_info)
        self.insert_flag = 0
        self.read_error_count = 0
        self.read_error_flag = 0
    def all_path(self, dirname):

        result = []  # 所有的文件

        for maindir, subdir, file_name_list in os.walk(dirname):

            print("1:", maindir)  # 当前主目录
            print("2:", subdir)  # 当前主目录下的所有目录
            print("3:", file_name_list)  # 当前主目录下的所有文件

            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                result.append(apath)

        return result
    def read_csv(self, filename, header=False):
        res = []
        count = 0
        with open(filename, encoding='gbk') as f:
            f_csv = csv.reader(f, delimiter=',')
            if header:
                headers = next(f_csv)
                header = False
            for row in f_csv:
                    res.append(row)
        return res
    def query_data(self):
        sql_read = ("SELECT * FROM pos367_data.pos367_ackey_map_manufacturedate where DevKey = '%s'")
        self.cursor.execute(sql_read)
        dev_results = self.cursor.fetchall()
        f = open('./outputfile/newInventorylist.csv', 'w+', newline='', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["DevKey", "Tim_stamp1", "PrSpeed", "Tim_stamp2"])
        for dev_result in dev_results:
            print(dev_result['DevKey'][0:3])
            if dev_result['DevKey'][0:3] >= "Pb2":
                sql_read2 = ("SELECT id_inc,time_stamp FROM soc_test_data.ba_obj_point where DevKey = '%s' and Obj_value = 180 and Obj_name = 'PrSpeed'"%(dev_result['DevKey']))
                print(dev_result['DevKey'])
                self.cursor.execute(sql_read2)
            dev_result2s = self.cursor.fetchall()
            for dev_result2 in dev_result2s:
                sql_read3 = ( "SELECT Obj_value,time_stamp FROM soc_test_data.ba_obj_point where id_inc = %d" % (dev_result2['id_inc']+1))
                self.cursor.execute(sql_read3)
                dev_result3 = self.cursor.fetchall()

                csv_writer.writerow([dev_result['DevKey'], dev_result2['time_stamp'].strftime("%Y-%m-%d %H:%M:%S"), str(dev_result3[0]['Obj_value']), dev_result3[0]['time_stamp'].strftime("%Y-%m-%d %H:%M:%S")])

        f.close()
    def query_data_from_csvfile(self,allfiles):
        for file in allfiles:
            dev_key = re.findall("csv[/](.*)\\\\", file)
            insert_data = []
            if '2021_06_14__10_56_28_inventory.csv' in file:
                f = open('./outputfile/newInventorylist.csv', 'w+', newline='', encoding='utf-8')
                csv_writer = csv.writer(f)
                csv_writer.writerow(["DevKey", "manufactureDate"])

                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    # sql_read = ("SELECT * FROM pos367_data.pos367_ackey_map_manufacturedate where DevKey = '%s'" %(data_result[1]))
                    # self.mydb.__cursor.execute(sql_read)
                    sql_results = self.mydb.select_some('pos367_data.pos367_ackey_map_manufacturedate','DevKey',data_result[1][:-1])
                    # dev_results = self.cursor.fetchall()
                    # self.dic_cloudinventorylist.append(data_result[1])
                    print("{0},{1}".format(sql_results[0]['DevKey'],sql_results[0]['factory_time_stamp'].strftime("%Y-%m-%d %H:%M:%S")))
                    csv_writer.writerow([sql_results[0]['DevKey'],sql_results[0]['factory_time_stamp'].strftime("%Y-%m-%d %H:%M:%S")])
                f.close()
            if 'SearchActivationKey.csv' in file:
                f = open('./outputfile/SearchActivationKey_Output_0818.csv', 'w+', newline='', encoding='utf-8')
                csv_writer = csv.writer(f)
                csv_writer.writerow(["DevKey", "manufactureDate"])

                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    # sql_read = ("SELECT * FROM pos367_data.pos367_ackey_map_manufacturedate where DevKey = '%s'" %(data_result[1]))
                    # self.mydb.__cursor.execute(sql_read)
                    sql_results = self.mydb.select_some('pos367_data.pos367_ackey_map_manufacturedate','DevKey',data_result[0])
                    # dev_results = self.cursor.fetchall()
                    # self.dic_cloudinventorylist.append(data_result[1])
                    print("{0},{1}".format(sql_results[0]['DevKey'],sql_results[0]['factory_time_stamp'].strftime("%Y-%m-%d %H:%M:%S")))
                    csv_writer.writerow([sql_results[0]['DevKey'],sql_results[0]['factory_time_stamp'].strftime("%Y-%m-%d %H:%M:%S")])
                f.close()


    def get_from_csv_insert_many(self, allfiles):
        for file in allfiles:
            dev_key = re.findall("csv[/](.*)\\\\", file)
            insert_data = []
            # self.dic_data['DevKey'] = dev_key[0]
            sql = "INSERT INTO pos367_ackey_map_manufactureDate(DevKey,factory_time_stamp) VALUES(%s,%s)"
            # if 'ActivationKey_ManufactureDate.csv' in file:
            if 'Activation key and manufacture date.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['DevKey'] = data_result[1]
                    self.dic_data['factory_time_stamp'] = data_result[2]
                    # self.dic_data['Obj_Property'] = self.Obj_Property[0]
                    # self.dic_data['Obj_name'] = self.Obj_name[0]
                    # self.dic_data['Obj_value'] = float(data_result[3])
                    # d = datetime.datetime.fromtimestamp(float(data_result[1])/1000)
                    # dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    # self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)

                    insert_data.append(tuple(temp_dic_data.values()))
                self.mydb.insert_many(sql, insert_data)
            elif 'RotExchMotorPresentSpeed.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['Obj_type'] = self.Obj_type[1]
                    self.dic_data['Obj_Ins'] = self.Obj_Ins[1]
                    self.dic_data['Obj_Property'] = self.Obj_Property[1]
                    self.dic_data['Obj_name'] = self.Obj_name[1]
                    self.dic_data['Obj_value'] = float(data_result[3])
                    d = datetime.datetime.fromtimestamp(float(data_result[1])/1000)
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)
                    insert_data.append(tuple(temp_dic_data.values()))
                self.mydb.insert_many(sql, insert_data)
            elif 'RotatingHeatExchanger.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['Obj_type'] = self.Obj_type[2]
                    self.dic_data['Obj_Ins'] = self.Obj_Ins[2]
                    self.dic_data['Obj_Property'] = self.Obj_Property[2]
                    self.dic_data['Obj_name'] = self.Obj_name[2]
                    self.dic_data['Obj_value'] = float(data_result[3])
                    d = datetime.datetime.fromtimestamp(float(data_result[1])/1000)
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)
                    insert_data.append(tuple(temp_dic_data.values()))
                self.mydb.insert_many(sql, insert_data)
    def get_from_csv(self, allfiles):
        for file in allfiles:
            dev_key = re.findall("csv[/](.*)\\\\", file)
            self.dic_data['DevKey'] = dev_key[0]
            insert_data = []
            if 'heat exchanger.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['Obj_type'] = self.Obj_type[0]
                    self.dic_data['Obj_Ins'] = self.Obj_Ins[0]
                    self.dic_data['Obj_Property'] = self.Obj_Property[0]
                    self.dic_data['Obj_name'] = self.Obj_name[0]
                    self.dic_data['Obj_value'] = float(data_result[3])
                    d = datetime.datetime.fromtimestamp(float(data_result[1]) / 1000)
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)
                    insert_data.append(temp_dic_data)
                self.mydb.insert('ba_obj_point', insert_data)
            elif 'present speed.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['Obj_type'] = self.Obj_type[1]
                    self.dic_data['Obj_Ins'] = self.Obj_Ins[1]
                    self.dic_data['Obj_Property'] = self.Obj_Property[1]
                    self.dic_data['Obj_name'] = self.Obj_name[1]
                    self.dic_data['Obj_value'] = float(data_result[3])
                    d = datetime.datetime.fromtimestamp(float(data_result[1]) / 1000)
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)
                    insert_data.append(temp_dic_data)
                self.mydb.insert('ba_obj_point', insert_data)
            elif 'pres.coil current.csv' in file:
                data_results = self.read_csv(file, True)
                for data_result in data_results:
                    self.dic_data['Obj_type'] = self.Obj_type[2]
                    self.dic_data['Obj_Ins'] = self.Obj_Ins[2]
                    self.dic_data['Obj_Property'] = self.Obj_Property[2]
                    self.dic_data['Obj_name'] = self.Obj_name[2]
                    self.dic_data['Obj_value'] = float(data_result[3])
                    d = datetime.datetime.fromtimestamp(float(data_result[1]) / 1000)
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")
                    self.dic_data['time_stamp'] = dt
                    temp_dic_data = copy.deepcopy(self.dic_data)
                    insert_data.append(temp_dic_data)
                self.mydb.insert('ba_obj_point', insert_data)

    def ProcessMotorReadLogic(self):
        request_list = []
        item = str(self.Obj_type[0]) + " " + str(self.Obj_Ins[0]) + " " + str(self.Obj_Property[0])
        request_list.append(item)
        item = str(self.Obj_type[1]) + " " + str(self.Obj_Ins[1]) + " " + str(self.Obj_Property[1])
        request_list.append(item)
        item = str(self.Obj_type[2]) + " " + str(self.Obj_Ins[2]) + " " + str(self.Obj_Property[2])
        request_list.append(item)
        insert_data = []
        insert_data_error = []
        temp_dic_data_old = []
        while 1:
            try:
                data_result = self.tt.read_multiple(self.bb[1], self.deviceIP, request_list)
                if len(data_result) == 3:
                    self.read_count = 0
                    print(111111111111111)
                    time_local = datetime.datetime.now()
                    timestamp = datetime.datetime.strftime(time_local, '%Y-%m-%d %H:%M:%S')
                    if self.read_error_flag == 2:
                        insert_data_error = []
                        self.dev_error['DevKey'] = self.DevKey
                        self.dev_error['Online'] = 'online'
                        self.dev_error['Tim_stamp'] = timestamp
                        temp_dic_data = copy.deepcopy(self.dev_error)
                        insert_data_error.append(temp_dic_data)
                        self.mydb.insert('devofflineevent', insert_data_error)
                        self.read_error_flag = 0

                    for i in range(0, 3):
                        self.dic_data['DevKey'] = self.DevKey
                        self.dic_data['Obj_type'] = self.Obj_type[i]
                        self.dic_data['Obj_Ins'] = self.Obj_Ins[i]
                        self.dic_data['Obj_Property'] = self.Obj_Property[i]
                        self.dic_data['Obj_name'] = self.Obj_name[i]
                        self.dic_data['Obj_value'] = float(data_result[i])
                        self.dic_data['time_stamp'] = timestamp
                        temp_dic_data = copy.deepcopy(self.dic_data)
                        print(float(data_result[i]))
                        if self.insert_flag == 0:
                            temp_dic_data_old.append(temp_dic_data)
                            insert_data.append(temp_dic_data)
                            self.cnt = self.cnt + 1
                        elif abs(temp_dic_data['Obj_value'] - temp_dic_data_old[i]['Obj_value']) > 0.01:
                            temp_time = time_local.timestamp()
                            temp_time = temp_time - 1
                            d = datetime.datetime.fromtimestamp(temp_time)
                            dt = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
                            temp_dic_data_old[i]['time_stamp'] = dt
                            insert_data.append(temp_dic_data_old[i])
                            temp_dic_data_old[i] = copy.deepcopy(temp_dic_data)
                            insert_data.append(temp_dic_data)
                            self.cnt = self.cnt + 1
                    self.insert_flag = 1
                    print(self.cnt)
                    if self.cnt >= 10:
                        self.mydb.insert('ba_obj_point_test', insert_data)
                        insert_data = []
                        self.cnt = 0
                else:
                    # error
                    print(222222222)
                    self.read_error_count = self.read_error_count + 1
                    if self.read_error_count > 3 and self.read_error_flag == 0:
                        self.read_error_flag = 1
                    if self.read_error_flag == 1:
                        self.read_error_flag = 2
                        insert_data_error = []
                        time_local = datetime.datetime.now()
                        timestamp = datetime.datetime.strftime(time_local, '%Y-%m-%d %H:%M:%S')
                        self.dev_error['DevKey'] = self.DevKey
                        self.dev_error['Online'] = 'offline'
                        self.dev_error['Tim_stamp'] = timestamp
                        temp_dic_data = copy.deepcopy(self.dev_error)
                        insert_data_error.append(temp_dic_data)
                        self.mydb.insert('devofflineevent', insert_data_error)
            except Exception as e:
                print(e)
            time.sleep(2)
    def dev_csv_to_sql(self):
        data_results = self.read_csv('Device_Database_File.csv', True)
        insert_data = []
        for data_result in data_results:
            self.dic_data['PlantID'] = data_result[0]
            self.dic_data['AppSoftVer'] = data_result[1]
            self.dic_data['FirmwareRevision'] = data_result[2]
            self.dic_data['ModelName'] = data_result[3]
            self.dic_data['ModelInformation'] = data_result[4]
            self.dic_data['ActivationKey'] = data_result[5]
            temp_dic_data = copy.deepcopy(self.dic_data)
            insert_data.append(temp_dic_data)
        self.mydb.insert('Device_DB', insert_data)
    def ResultData_csv_to_sql(self):
        data_results = self.read_csv('./outputfile/ResultMaxMin1.csv', True)
        insert_data = []
        for data_result in data_results:
            self.dic_data['PlantID'] = data_result[0]
            self.dic_data['Tim_stamp1'] = data_result[1]
            self.dic_data['PrSpeed'] = data_result[2]
            self.dic_data['Tim_stamp2'] = data_result[3]
            self.dic_data['CoilMax'] = float(data_result[4])
            self.dic_data['CoilMin'] = float(data_result[5])
            temp_dic_data = copy.deepcopy(self.dic_data)
            insert_data.append(temp_dic_data)
        self.mydb.insert('ResultMaxMin', insert_data)
    def DevCoilData_csv_to_sql(self):

        data_results = self.read_csv('./outputfile/devresult.csv', True)
        insert_data = []
        for data_result in data_results:
            self.dic_data['PlantID'] = data_result[0]
            self.dic_data['CoilMax'] = float(data_result[1])
            self.dic_data['CoilMin'] = float(data_result[2])
            temp_dic_data = copy.deepcopy(self.dic_data)
            insert_data.append(temp_dic_data)
        self.mydb.insert('DevResultMaxMin', insert_data)
if __name__ == '__main__':
    configinfo = MotorTest()
    #configinfo.dev_csv_to_sql()
    #configinfo.ResultData_csv_to_sql()
    #configinfo.DevCoilData_csv_to_sql()
    all_files = configinfo.all_path('./ACK_ManufactureDate/')
    # configinfo.get_from_csv_insert_many(all_files)
    configinfo.query_data_from_csvfile(all_files)

