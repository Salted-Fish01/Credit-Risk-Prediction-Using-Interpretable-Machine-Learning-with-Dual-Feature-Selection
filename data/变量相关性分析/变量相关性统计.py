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
#变量相关性分析
cor=df.corr('spearman')
#转换为dataframe结构
df_cor=pd.DataFrame(cor)
df_cor.to_excel("变量相关性分析.xlsx")

#列出高于0.8正相关或小于-0.8负相关的系数矩阵
high_cor=cor[(cor>0.8)|(cor<-0.8)]
cor.loc[:,:]=np.tril(cor,k=-1)
cor=cor.stack()
#仅仅列出高相关系数，数据呈现结构化
high_cor1=cor[(cor>0.8)|(cor<-0.8)]

df_high_cor1=pd.DataFrame(high_cor1)
#保存到Excel
df_high_cor1.to_excel("高相关性变量汇总.xlsx")







