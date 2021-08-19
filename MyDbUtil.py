import pymysql
class MyDbUtil(object):
    def __init__(self,mysql_info):
        self._conn = pymysql.connect(host=mysql_info["host"],
                                     user=mysql_info["user"],
                                     password=mysql_info["password"],
                                     charset=mysql_info["charset"],
                                     port=mysql_info["port"],
                                     cursorclass=pymysql.cursors.DictCursor)

        self.__cursor = self._conn.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pos367_data")
        self._conn.commit()
        self.inert_count = 0
        self.__cursor.execute("use pos367_data;")
        sql = """CREATE TABLE IF NOT EXISTS `pos367_ackey_map_manufactureDate` (
              `id_inc` int NOT NULL AUTO_INCREMENT,
              `DevKey` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
              `factory_time_stamp` datetime NOT NULL,
              PRIMARY KEY (`id_inc`)
            ) """
        self.__cursor.execute(sql)
        self._conn.commit()
        # sql = """CREATE TABLE IF NOT EXISTS `ba_obj_point_test` (
        #       `id_inc` int NOT NULL AUTO_INCREMENT,
        #       `DevKey` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
        #       `Obj_type` int NOT NULL,
        #       `Obj_Ins` int NOT NULL,
        #       `Obj_Property` int NOT NULL,
        #       `Obj_name` varchar(20) NOT NULL,
        #       `Obj_value` float NOT NULL,
        #       `time_stamp` datetime NOT NULL,
        #       PRIMARY KEY (`id_inc`)
        #     ) """
        # self.__cursor.execute(sql)
        # self._conn.commit()
        # sql = """CREATE TABLE IF NOT EXISTS `Device_DB` (
        #       `PlantID` char(100),
        #       `AppSoftVer` char(100),
        #       `FirmwareRevision` char(100),
        #       `ModelName` char(100),
        #       `ModelInformation` char(100),
        #       `ActivationKey` char(100),
        #       PRIMARY KEY (`PlantID`)
        #     ) """
        # self.__cursor.execute(sql)
        # self._conn.commit()

        # sql = """CREATE TABLE IF NOT EXISTS `DevOfflineEvent` (
        #       `id_inc` int NOT NULL AUTO_INCREMENT,
        #       `DevKey` char(50),
        #       `Online` char(20),
        #       `Tim_stamp` datetime,
        #       PRIMARY KEY (`id_inc`)
        #     ) """
        # self.__cursor.execute(sql)
        # self._conn.commit()
    def close_db(self):
        self.__cursor.close()
        self._conn.close()
    def create_db(self,dbname):
        sql = "CREATE DATABASE IF NOT EXISTS {db_create}".format(db_create=dbname)
        self.__cursor.execute(sql)
        self._conn.commit()
    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS `ba_obj_point` (
              `id_inc` int(11) NOT NULL AUTO_INCREMENT,
              `DevKey` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
              `Obj_type` int(11) NOT NULL,
              `Obj_Ins` int(11) NOT NULL,
              `Obj_Property` int(11) NOT NULL,
              `Obj_name` varchar(20) NOT NULL,
              `Obj_value` float NOT NULL,
              `time_stamp` datetime NOT NULL,
              PRIMARY KEY (`id_inc`)
            ) """
        self.__cursor.execute(sql)
        self._conn.commit()
    def insert(self, table, insert_data):
        """
        :param table:
        :param insert_data  type:[{},{}]:
        :return:effect_row 1 影响的行数
        """
        try:
            for data in insert_data:
                key = ','.join(data.keys())
                values = map(self._deal_values, data.values())
                insert_data = ', '.join(values)
                sql = "insert into {table}({key}) values ({val})".format(table=table, key=key, val=insert_data)
                effect_row = self.__cursor.execute(sql)
                self._conn.commit()
            return effect_row
        except Exception as e:
            print(e)
        finally:
            # self.close_db()
            pass
    def insert_many(self, sql, insert_data_list):
        """
        :param table:
        :param insert_data  type:[{},{}]:
        :return:effect_row 1 影响的行数
        """
        try:
            len = self.__cursor.executemany(sql, insert_data_list)
            print(len)
            self._conn.commit()
        except Exception as e:
            print(e)
        finally:
            # self.close_db()
            pass

    def delete(self, table, condition):
        """
        :param table:
        :param condition type{"":""}:
        :return effect_row 1 影响的行数:
        """
        condition_list = self._deal_values(condition)
        condition_data = ' and '.join(condition_list)
        sql = "delete from {table} where {condition}".format(table=table, condition=condition_data)
        effect_row = self.__cursor.execute(sql)
        self._conn.commit()
        # self.close_db()
        return effect_row

    def update(self, table, data, condition=None):
        """
        :param table:
        :param data type 字典 {}:
        :param condition tpye 字典 {}:
        :return:
        """
        update_list = self._deal_values(data)
        update_data = ",".join(update_list)
        if condition is not None:
            condition_list = self._deal_values(condition)
            condition_data = ' and '.join(condition_list)
            sql = "update {table} set {values} where {condition}".format(table=table, values=update_data,
                                                                         condition=condition_data)
        else:
            sql = "update {table} set {values}".format(table=table, values=update_data)
        effect_row = self.__cursor.execute(sql)
        self._conn.commit()
        # self.close_db()
        return effect_row

    def select_id(self, table, id):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :param get_one bool:
        :return:
        """
        sql = "select * from {table} where id = {id}".format(table=table, id=id)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_some(self, table, filed, value):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :return:
        """
        sql = "select * from {table} where {filed} = '{value}'".format(table=table, filed=filed, value=value)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_all(self, table):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :return:
        """
        sql = "select * from {table}".format(table=table)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def query_sql(self, sql):
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        if result:
            return result
        else:
            return None
    def db_commit(self, sql):
        self._conn.commit()
    def _deal_values(self, value):
        """
        self._deal_values(value) -> str or list
            处理传进来的参数
        """
        # 如果是字符串则加上''
        if isinstance(value, str):
            value = ("'{value}'".format(value=value))
        # 如果是字典则变成key=value形式
        elif isinstance(value, dict):
            result = []
            for key, value in value.items():
                value = self._deal_values(value)
                res = "{key}={value}".format(key=key, value=value)
                result.append(res)
            return result
        else:
            value = (str(value))
        return value

# if __name__:
#     mydb = MyDbUtil()
#     rs = mydb.query_sql("select * from ba_obj_point")
#     print(rs)