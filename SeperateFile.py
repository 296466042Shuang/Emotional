import os

# 设置新文件的保存路径
save_path = 'new_folder'
# 如果这个文件夹不存在，创建一个新的
if not os.path.exists(save_path):
    os.makedirs(save_path)

file_number = 1
current_file = None

with open('F:\PythonProject\EmotionalAnalysis\Data\TEST.CSV', 'r') as f:
    for line in f:
        # 如果当前行是 'Time, HR, GSR'，开始一个新的文件
        if line.strip() == 'Time, HR, GSR':
            # 如果当前文件存在，关闭它
            if current_file is not None:
                current_file.close()
            # 创建一个新的文件并开始写入
            current_file = open(os.path.join(save_path, f'{file_number}.csv'), 'w')
            current_file.write(line)  # 写入表头
            print(f"Created new file: {os.path.join(save_path, f'{file_number}.csv')}")
            file_number += 1
        # 否则，将当前行写入当前文件
        elif current_file is not None:
            current_file.write(line)

# 如果最后一个文件还没有被关闭，关闭它
if current_file is not None:
    current_file.close()
