# Author: Zhi Kai
# Time:  0:25
import numpy as np
from datetime import datetime
from pyhrv.time_domain import time_domain
from pyhrv.frequency_domain import frequency_domain
from pyhrv.nonlinear import nonlinear

# 定义心率数据文件名
filename = 'heart_rate_data.txt'

# 读取心率数据文件
with open(filename, 'r') as f:
    lines = f.readlines()

# 创建一个时间戳数组和一个心率数组
timestamps = []
hr_values = []

# 从文件中提取时间戳和心率数据
for line in lines:
    parts = line.split(',')
    timestamp = datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
    hr_value = int(parts[1])
    timestamps.append(timestamp)
    hr_values.append(hr_value)

# 将心率数据转换为numpy数组
hr_values = np.array(hr_values)

# 计算时间域特征
time_features = time_domain(hr_values)

# 计算频率域特征
freq_features = frequency_domain(hr_values)

# 计算非线性特征
len(hr_values)
nonlinear_features = nonlinear(hr_values)

# 输出特征结果
print('Time domain features:')
for key, value in time_features.items():
    print(f'{key}: {value}')

print('Frequency domain features:')
for key, value in freq_features.items():
    print(f'{key}: {value}')

print('Nonlinear features:')
for key, value in nonlinear_features.items():
    print(f'{key}: {value}')
