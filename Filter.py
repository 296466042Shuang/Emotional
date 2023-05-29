# Author: Zhi Kai
# Time:  14:50
import os
import pandas as pd


def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            try:
                data = pd.read_csv(file_path, error_bad_lines=False)

                # 检查数据文件的最大时间值是否小于120
                if data['Time'].max() < 120:
                    print(f"{filename} skipped as it does not reach the specified time length.")
                    continue

                # 筛选出时间小于120秒的数据
                data_filtered = data[(data['Time'] >= 0) & (data['Time'] <= 120)]

                # 将筛选后的数据保存到新的CSV文件中
                output_path = os.path.join(output_folder, f"filtered_{filename}")
                data_filtered.to_csv(output_path, index=False)
                print(f"Filtered data saved to {output_path}")

            except pd.errors.ParserError:
                print(f"Error parsing {filename}. Skipping.")
        else:
            print(f"{filename} is not a CSV file. Skipping.")


input_folder = 'F:\PythonProject\EmotionalAnalysis\\new_folder'
output_folder = 'F:\PythonProject\EmotionalAnalysis\\filter'
process_files(input_folder, output_folder)