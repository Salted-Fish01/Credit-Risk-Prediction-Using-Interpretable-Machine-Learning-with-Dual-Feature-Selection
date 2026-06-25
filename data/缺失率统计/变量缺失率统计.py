# -*- coding: utf-8 -*-
"""
描述性统计脚本
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from sklearn import metrics
 
#读取文件，去掉-999的单元格
readFileName="data.xlsx"
#读取excel
df=pd.read_excel(readFileName)
#描述性统计
df.describe()
def Variable_distribution(thedf,variable):
    series_variable=thedf[variable]
    distribution=series_variable.value_counts()
    return distribution
 
 
#查看字段缺失率
def Missing_percentage(the_df):
    #字段行总数
    total=df.shape[0]
    #各个字段计数
    count=df.count()
    #空缺率
    miss_percentage=1-count/total*1.0
    return miss_percentage
#缺失率大于百分之50的字段过滤
 
 
#查看字段缺失率
#df.info()
miss_percentage=Missing_percentage(df)
#print("missing percentages:",miss_percentage)
#缺失率大于百分之五十的字段过滤
fiter=0.5
columns=['变量缺失率']
df_missing=pd.DataFrame(miss_percentage,columns=columns)
df_missing_filter=df_missing[df_missing['变量缺失率']>fiter]
print("变量缺失率>%f"%fiter)
print(df_missing_filter)
df_missing.to_excel("变量缺失率汇总.xlsx")
df_missing_filter.to_excel("高缺失率变量汇总.xlsx")
 






