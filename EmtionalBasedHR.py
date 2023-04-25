import numpy as np
import openpyxl

# 从.xlsx文件中读取心率数据
file_name = "F:\PythonProject\EmotionalAnalysis\Data\\record_1.xlsx"
wb = openpyxl.load_workbook(file_name)
sheet = wb.active

hr_data = []
for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过表头
    hr_data.append((int(row[0]), int(row[1])))

# 过滤掉为0的数据
filtered_hr_data = [hr for _, hr in hr_data if int(hr) > 0]

# 计算心率差值
hr_diff = np.diff(filtered_hr_data)

# 计算RMSSD
rmssd = np.sqrt(np.mean(np.square(hr_diff)))

print(f"RMSSD: {rmssd}")
