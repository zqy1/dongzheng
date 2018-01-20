# -*- coding:utf-8 -*-

"""
数据类型转换example
df['col2'] = df['col2'].astype('int')
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# file_name = 'data/con_ba_test_part.tsv'
file_name = '/home/zqy/东证期货杯/data_part/con_ext_crd_hd_report_part.csv'
with open(file_name, encoding='utf-8') as f:
    # 利用pandas读取csv, tsv数据
    # 对csv, tsv进行相应分隔
    if file_name.split('.')[-1] == 'csv':
        f_csv = pd.read_csv(f)
    elif file_name.split('.')[-1] == 'tsv':
        f_csv = pd.read_csv(f, delimiter='\t')

    print(f_csv)
    print(f_csv.columns)

    # print(type(f_csv['REPORT_ID']))
    # 每一列都是一个series, < class 'pandas.core.series.Series'>
    print(f_csv['REPORT_ID'].dtype)
    # 修改pandas列的数据类型
    f_csv['REPORT_ID'] = f_csv['REPORT_ID'].astype('object')
    # f_csv['REPORT_ID'] = f_csv['REPORT_ID'].astype('object')
    # print(f_csv['REPORT_ID'].dtype)
    # print(f_csv.describe())

