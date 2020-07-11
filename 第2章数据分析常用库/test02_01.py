#导入包并重命名np
import numpy as np

#定义一维数组
a = np.array([2, 0, 1, 5, 8, 3])
print(u'原始数据:', a)

#输出最大、最小值及形状
print(u'最小值:', a.min())
print(u'最大值:', a.max())
print(u'形状', a.shape)
