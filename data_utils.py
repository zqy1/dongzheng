# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DataUtils:

    # 实例化时传入文件名(含路径)
    def __init__(self, file_name):
        self.file_name = file_name

    # DataUtils类的私有方法,读取csv,tsv文件，返回DataFrame数据格式的内容
    def __read_csv(self):
        with open(self.file_name, encoding='utf-8') as f:
            # 利用pandas读取csv, tsv数据
            # 对csv, tsv进行相应分隔
            if self.file_name.split('.')[-1] == 'csv':
                f_csv = pd.read_csv(f)
                return f_csv
            elif self.file_name.split('.')[-1] == 'tsv':
                f_csv = pd.read_csv(f, delimiter='\t')
                return f_csv

    # 显示数据默认显示前5行
    def data_show(self, start=0, end=5):
        f_csv = self.__read_csv()
        return f_csv[start:end]

    # 数据描述
    def data_describe(self, name):
        f_csv = self.__read_csv()
        try:
            line_num = f_csv[name].count()
            set_name = set(f_csv[name])
            uid_num = len(set(f_csv[name]))
        except KeyError:
            line_num = f_csv[name.lower()].count()
            set_name = set(f_csv[name.lower()])
            uid_num = len(set(f_csv[name.lower()]))

        describe = '共' + str(line_num) + '条数据' + '\n' + '共'+ str(uid_num) +'个不同列' + str(set_name)
        return describe

    def get_dtypes(self):
        f_csv = self.__read_csv()
        # print(f_csv.columns)
        print(f_csv.dtypes)

    def set_dtypes(self, dtype_dict: dict):
        f_csv = self.__read_csv()
        print(f_csv[dtype_dict.keys()])
        # f_csv[dtype_dict.keys()] = f_csv['REPORT_ID'].astype('object')

    def test_list(self, ke: list) -> list:
        return ke+[1,1]

    # def greeting(self, name: str) -> str:
    #     return 'Hello ' + name


if __name__ == '__main__':

    data = DataUtils('/home/zqy/东证期货杯/data/contest_ext_crd_cd_ln_spl.tsv')
    # data = DataUtils('/home/zqy/东证期货杯/data/contest_ext_crd_cd_ln.tsv')

    h = data.data_describe('type_dw')
    print(h)

    # data.get_dtypes()

    # data.set_dtypes({'WORK_PROVINCE':'int64'})
    m = data.test_list([1,2,3])
    print(m)
    # print(data.greeting(12))