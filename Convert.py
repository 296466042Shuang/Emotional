import os
import pandas as pd

# 指定原始文件夹和目标文件夹
input_dir = 'F:\PythonProject\EmotionalAnalysis\OpenSingal'  # 用你的输入文件夹路径替换
output_dir = 'F:\PythonProject\EmotionalAnalysis\OpenSingal\csv'  # 用你的输出文件夹路径替换

# 检查输出目录是否存在，如果不存在，则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入文件夹中的每个文件
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):  # 只处理txt文件
        # 拼接完整的文件路径
        file_path = os.path.join(input_dir, filename)
        # 读取文件并转换为数据框
        df = pd.read_csv(file_path, sep="\t", comment="#", names=["nSeq","I1","I2","O1","O2","A1","A2","A3","A4","A5","A6"])
        # 创建新的文件名（将.txt更改为.csv）
        new_filename = filename.replace('.txt', '.csv')
        # 拼接输出文件路径
        output_path = os.path.join(output_dir, new_filename)
        # 保存为csv文件
        df.to_csv(output_path, index=False)