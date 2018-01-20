# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os

def dir_info():
    current_dir = os.getcwd()
    # print(current_dir)
    
    if os.path.exists(current_dir + '/data') == True:
        data_dir_files = os.listdir(current_dir + '/data')
    
        data_csv_files = []
        for file in data_dir_files:
            if file.split('.')[-1] == 'csv' or file.split('.')[-1] == 'tsv':
                data_csv_files.append(file)
        print(data_csv_files)

        for i in data_csv_files:
            csv_path = current_dir + '/data/' +i
            print(csv_path)
        # print(len(data_csv_files))


def judge_delimiter(file_name):
    with open(file_name, encoding='utf-8') as f:
        # 利用pandas读取csv, tsv数据
        # 对csv, tsv进行相应分隔
        if file_name.split('.')[-1] == 'csv':
            f_csv = pd.read_csv(f)
            delimiter = ','
            return delimiter
        elif file_name.split('.')[-1] == 'tsv':
            f_csv = pd.read_csv(f, delimiter='\t')
            delimiter = '\t'
            return delimiter

# 传入一个已经读取的csv文件,将该文件列名大写后返回该文件
def columns_upper(datasheet):
    cloumns_uppered = []
    for i in datasheet.columns:
        cloumns_uppered.append(i.upper())

    datasheet.columns = cloumns_uppered
    return datasheet


# 组合两份csv文件
def merage(first_data_path, second_data_path, first_delimiter, second_delimiter):
    first_datasheet = pd.read_csv(first_data_path, delimiter=first_delimiter)
    first_datasheet_upper = columns_upper(first_datasheet)


    second_datasheet = pd.read_csv(second_data_path, delimiter=second_delimiter)
    second_datasheet_upper = columns_upper(second_datasheet)

    # result_datasheet = pd.merge(first_datasheet, second_datasheet, how=
    # 'outer', on='REPORT_ID')

    # 不应该使用外连接
    # result_datasheet = pd.merge(first_datasheet_upper, second_datasheet_upper, how=
    # 'outer', on='REPORT_ID')
    result_datasheet = pd.merge(first_datasheet_upper, second_datasheet_upper, how=
    'left', on='REPORT_ID')

    result_datasheet.to_csv('/home/zqy/东证期货杯/data_deal/data_left_outer2.tsv',sep='\t',index=False)
    print(result_datasheet)
    
if __name__ == '__main__':
    # dir_info()

    # first = '/home/zqy/东证期货杯/data/contest_basic_train.tsv'
    # second = '/home/zqy/东证期货杯/data/contest_ext_crd_cd_ln.tsv'

    # # 左连接output:[248345 rows x 32 columns]
    # # 外连接output: [360962 rows x 32 columns]


    first = '/home/zqy/东证期货杯/data_deal/data_left_outer1.tsv'
    second = '/home/zqy/东证期货杯/data/contest_ext_crd_cd_ln_spl.tsv'


    merage(first, second, judge_delimiter(first), judge_delimiter(second))



