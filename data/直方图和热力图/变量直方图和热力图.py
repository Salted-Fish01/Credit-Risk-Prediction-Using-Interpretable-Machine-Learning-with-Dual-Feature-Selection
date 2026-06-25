# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:40:33 2018

作者邮箱231469242@qq.com
微信公众号：python风控模型
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown, Latex
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#中文乱码问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
 
#读取文件
readFileName="data.xlsx"
#读取excel
df=pd.read_excel(readFileName)

#直方图
df.hist(figsize=(20,15))
plt.savefig("变量直方图.png")
plt.show()

matrix_cor=df.corr().round(2)
plt.figure(figsize=(20,15))
sns.heatmap(matrix_cor)
plt.savefig("变量热力图.png")
plt.show()






























