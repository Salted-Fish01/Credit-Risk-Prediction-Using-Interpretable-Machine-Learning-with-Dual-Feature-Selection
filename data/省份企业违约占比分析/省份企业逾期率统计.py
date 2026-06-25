# -*- coding: utf-8 -*-
"""
@author:231469242@qq.com

"""

import toad
from toad.plot import bin_plot
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection  import cross_val_score
#import statsmodels.api as sm
#混淆矩阵计算
from sklearn import metrics
from sklearn.metrics import roc_curve, auc,roc_auc_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

#读取原始数据-分析省份和市
df = pd.read_excel('data.xlsx')
#读取excel
x=df.loc[:,"省份":"总资产周转率"]
y=df["是否违约"]

# 计算每个省份的坏客户数量和总客户数量
province_bad_counts = df.groupby('省份')['是否违约'].sum()
province_total_counts = df.groupby('省份')['是否违约'].count()

# 计算每个省份的坏客户占比
province_bad_ratio = province_bad_counts / province_total_counts
print(province_bad_ratio)
df_province=pd.DataFrame(province_bad_ratio)
df_province.to_excel("各省违约率.xlsx")







