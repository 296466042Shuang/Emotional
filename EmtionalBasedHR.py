import numpy as np
import openpyxl

import os
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

folder_path = "F:\PythonProject\EmotionalAnalysis\Data"
rmssd_list = []
file_count = 0

for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_count += 1
        file_name = os.path.join(folder_path, file)
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active

        hr_data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过表头
            if str(row[0]).isdigit() and str(row[1]).isdigit():
                hr_data.append((int(row[0]), int(row[1])))

        # 过滤掉为0的数据
        filtered_hr_data = [hr for _, hr in hr_data if int(hr) > 0]

        # 计算心率差值
        hr_diff = np.diff(filtered_hr_data)

        # 计算RMSSD
        rmssd = np.sqrt(np.mean(np.square(hr_diff)))

        print(f"File {file_count}: HRV: {rmssd}")
        rmssd_list.append(rmssd)

# 绘制RMSSD值
plt.plot(range(1, file_count + 1), rmssd_list)
plt.xlabel('File Number')
plt.ylabel('RMSSD')
plt.title('RMSSD Values for All Files')
plt.show()
