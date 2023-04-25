# Author: Zhi Kai
# Time:  0:07
import numpy as np
import openpyxl
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 从Excel文件中读取数据
file_name = "F:\PythonProject\EmotionalAnalysis\Data\\record_1.xlsx"
wb = openpyxl.load_workbook(file_name)
sheet = wb.active

data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    data.append([float(value) for value in row])

# 数据预处理：标准化
scaler = StandardScaler()
data = scaler.fit_transform(data)

# 使用K-means聚类算法
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data)

# 获取聚类结果
labels = kmeans.labels_

# 打印聚类结果
for i, label in enumerate(labels):
    print(f"Data point {i + 1}: Cluster {label + 1}")
