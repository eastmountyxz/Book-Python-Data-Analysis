#encoding=utf-8
import pandas as pd

#读取数据 header设置Excel无标题头
data = pd.read_excel("test02.xls", header=None) 
print(data)

#计算数据长度
print(u'行数', len(data))
#计算用户A\B\C消费求和
print(data.sum())
#计算用户A\B\C消费算术平均数
mm = data.sum()
print(mm)
#输出预览前5行数据
print(u'预览前5行数据')
print(data.head())

#输出数据基本统计量  
print(u'输出数据基本统计量')
print(data.describe())
